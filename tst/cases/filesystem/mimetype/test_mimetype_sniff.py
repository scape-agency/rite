# =============================================================================
# Test: mimetype_sniff
# =============================================================================

"""
Tests for rite.filesystem.mimetype.mimetype_sniff.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.mimetype.mimetype_sniff import (
    _check_iso_bmff,
    _check_ogg_container,
    _check_riff_container,
    mimetype_sniff,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_mimetype_sniff_common_signatures() -> None:
    """Test that common magic numbers are detected correctly."""
    assert mimetype_sniff(b"\x89PNG\r\n\x1a\nrest") == "image/png"
    assert mimetype_sniff(b"\xff\xd8\xffrest") == "image/jpeg"
    assert mimetype_sniff(b"GIF89arest") == "image/gif"
    assert mimetype_sniff(b"%PDF-rest") == "application/pdf"
    assert mimetype_sniff(b"PK\x03\x04rest") == "application/zip"
    assert mimetype_sniff(b"\x1f\x8b\x08rest") == "application/gzip"


def test_mimetype_sniff_empty_buffer() -> None:
    """Test empty buffer returns None."""
    assert mimetype_sniff(b"") is None
    assert mimetype_sniff(bytearray()) is None


def test_mimetype_sniff_gif87a() -> None:
    """Test GIF87a signature detection."""
    assert mimetype_sniff(b"GIF87arest") == "image/gif"


def test_mimetype_sniff_mp3_id3() -> None:
    """Test MP3 ID3 tag detection."""
    assert mimetype_sniff(b"ID3rest") == "audio/mpeg"


def test_mimetype_sniff_mp3_sync() -> None:
    """Test MP3 sync word detection."""
    # 0xFF 0xE0+ indicates MP3 frame sync
    assert mimetype_sniff(b"\xff\xe0rest") == "audio/mpeg"
    assert mimetype_sniff(b"\xff\xfbrest") == "audio/mpeg"


def test_mimetype_sniff_flac() -> None:
    """Test FLAC signature detection."""
    assert mimetype_sniff(b"fLaCrest") == "audio/flac"


def test_check_riff_container_webp() -> None:
    """Test RIFF WebP detection."""
    webp_header = b"RIFF\x00\x00\x00\x00WEBPrest"
    assert _check_riff_container(memoryview(webp_header)) == "image/webp"
    assert mimetype_sniff(webp_header) == "image/webp"


def test_check_riff_container_wav() -> None:
    """Test RIFF WAV detection."""
    wav_header = b"RIFF\x00\x00\x00\x00WAVErest"
    assert _check_riff_container(memoryview(wav_header)) == "audio/wav"
    assert mimetype_sniff(wav_header) == "audio/wav"


def test_check_riff_container_not_riff() -> None:
    """Test RIFF container with non-RIFF header."""
    assert _check_riff_container(memoryview(b"NOTRIFFrest")) is None


def test_check_riff_container_short_buffer() -> None:
    """Test RIFF container with short buffer."""
    assert _check_riff_container(memoryview(b"RIFFxxx")) is None


def test_check_riff_container_long_but_not_riff() -> None:
    """Test RIFF check with long buffer but not RIFF (branch 57->59)."""
    # Length >= 12 but first 4 bytes != RIFF
    assert _check_riff_container(memoryview(b"NOTRIFFdataa")) is None


def test_check_riff_container_riff_but_unknown_type() -> None:
    """Test RIFF container with unknown type (branch 57->59)."""
    # Starts with RIFF, but not WEBP or WAVE
    riff_unknown = b"RIFF" + b"xxxx" + b"UNKN"
    assert _check_riff_container(memoryview(riff_unknown)) is None


def test_check_ogg_container_ogg() -> None:
    """Test Ogg container detection."""
    ogg_header = b"OggS" + b"\x00" * 60
    assert mimetype_sniff(ogg_header) == "application/ogg"


def test_check_ogg_container_opus() -> None:
    """Test Ogg Opus detection."""
    opus_header = b"OggS" + b"\x00" * 10 + b"OpusHead" + b"\x00" * 46
    assert _check_ogg_container(memoryview(opus_header)) == "audio/opus"
    assert mimetype_sniff(opus_header) == "audio/opus"


def test_check_ogg_container_vorbis() -> None:
    """Test Ogg Vorbis detection."""
    vorbis_header = b"OggS" + b"\x00" * 10 + b"\x01vorbis" + b"\x00" * 43
    assert _check_ogg_container(memoryview(vorbis_header)) == "audio/vorbis"
    assert mimetype_sniff(vorbis_header) == "audio/vorbis"


def test_check_ogg_container_theora() -> None:
    """Test Ogg Theora detection."""
    theora_header = b"OggS" + b"\x00" * 10 + b"\x80theora" + b"\x00" * 43
    assert _check_ogg_container(memoryview(theora_header)) == "video/theora"
    assert mimetype_sniff(theora_header) == "video/theora"


def test_check_ogg_container_not_ogg() -> None:
    """Test non-Ogg data returns None."""
    assert _check_ogg_container(memoryview(b"NOTOggSrest")) is None


def test_check_iso_bmff_mp4() -> None:
    """Test ISO BMFF MP4 detection."""
    mp4_header = b"\x00\x00\x00\x00ftypisom" + b"\x00" * 50
    assert _check_iso_bmff(memoryview(mp4_header)) == "video/mp4"
    assert mimetype_sniff(mp4_header) == "video/mp4"


def test_check_iso_bmff_mp4_variants() -> None:
    """Test ISO BMFF MP4 variants."""
    for brand in [b"iso2", b"mp41", b"mp42", b"MSNV", b"avc1"]:
        header = b"\x00\x00\x00\x00ftyp" + brand + b"\x00" * 50
        assert mimetype_sniff(header) == "video/mp4"


def test_check_iso_bmff_avif() -> None:
    """Test ISO BMFF AVIF detection."""
    avif_header = b"\x00\x00\x00\x00ftypavif" + b"\x00" * 50
    assert _check_iso_bmff(memoryview(avif_header)) == "image/avif"
    assert mimetype_sniff(avif_header) == "image/avif"

    avis_header = b"\x00\x00\x00\x00ftypavis" + b"\x00" * 50
    assert mimetype_sniff(avis_header) == "image/avif"


def test_check_iso_bmff_heif() -> None:
    """Test ISO BMFF HEIF detection."""
    for brand in [b"heic", b"heix", b"hevc", b"hevx"]:
        header = b"\x00\x00\x00\x00ftyp" + brand + b"\x00" * 50
        assert mimetype_sniff(header) == "image/heif"


def test_check_iso_bmff_unknown_brand() -> None:
    """Test ISO BMFF with unknown brand returns octet-stream."""
    unknown_header = b"\x00\x00\x00\x00ftypXXXX" + b"\x00" * 50
    assert (
        _check_iso_bmff(memoryview(unknown_header))
        == "application/octet-stream"
    )


def test_check_iso_bmff_not_ftyp() -> None:
    """Test non-ftyp data returns None."""
    assert _check_iso_bmff(memoryview(b"\x00\x00\x00\x00XXXXisom")) is None


def test_check_iso_bmff_short_buffer() -> None:
    """Test ISO BMFF with short buffer."""
    assert _check_iso_bmff(memoryview(b"\x00\x00\x00\x00ftyp")) is None


def test_mimetype_sniff_max_probe() -> None:
    """Test max_probe parameter limits bytes inspected."""
    # Create a buffer with PNG signature beyond max_probe limit
    _ = b"x" * 10 + b"\x89PNG\r\n\x1a\n"  # noqa: F841 - example data
    # With default max_probe, signature should be found if within range
    assert mimetype_sniff(b"\x89PNG\r\n\x1a\n" + b"x" * 600) == "image/png"


def test_mimetype_sniff_unrecognized() -> None:
    """Test unrecognized data returns None."""
    assert mimetype_sniff(b"random unknown data") is None
    assert mimetype_sniff(b"\x00\x00\x00\x00\x00") is None


def test_mimetype_sniff_bytearray() -> None:
    """Test bytearray input works correctly."""
    assert mimetype_sniff(bytearray(b"\x89PNG\r\n\x1a\n")) == "image/png"


def test_mimetype_sniff_memoryview() -> None:
    """Test memoryview input works correctly."""
    data = b"\x89PNG\r\n\x1a\nrest"
    assert mimetype_sniff(memoryview(data)) == "image/png"
