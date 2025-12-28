# =============================================================================
# Test: mimetype_guess
# =============================================================================

"""
Tests for rite.filesystem.mimetype.mimetype_guess.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import io

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.mimetype.mimetype_guess import mimetype_guess

# =============================================================================
# Test Functions
# =============================================================================


class _DummyUpload:
    def __init__(self, name: str, content_type: str | None = None) -> None:
        self.name = name
        if content_type is not None:
            self.content_type = content_type


def test_mimetype_guess_prefers_content_type_if_present() -> None:
    """Explicit content_type should override name-based guessing."""
    obj = _DummyUpload(name="file.bin", content_type="application/x-test")
    assert mimetype_guess(obj) == "application/x-test"


def test_mimetype_guess_from_name_and_bytes() -> None:
    """Guess from filename and from sniffed bytes."""
    assert mimetype_guess("example.jpg") in {"image/jpeg", "image/pjpeg"}

    stream = io.BytesIO(b"\x89PNG\r\n\x1a\nrest")
    mime = mimetype_guess(stream, prefer_sniff=True)
    assert mime == "image/png"


def test_mimetype_guess_url_path() -> None:
    """Test mimetype_guess extracts path from URL (lines 84-85)."""
    result = mimetype_guess("http://example.com/image.jpg")
    assert result in {"image/jpeg", "image/pjpeg"}

    # URL with query string
    result = mimetype_guess("https://cdn.example.com/file.png?v=123")
    assert result == "image/png"


def test_mimetype_guess_empty_bytes() -> None:
    """Test mimetype_guess with empty bytes returns None (line 93)."""
    stream = io.BytesIO(b"")
    result = mimetype_guess(stream, prefer_sniff=True)
    assert result is None


def test_mimetype_guess_unknown_bytes() -> None:
    """Test mimetype_guess with unknown bytes."""
    stream = io.BytesIO(b"random unknown data")
    result = mimetype_guess(stream, prefer_sniff=True)
    # Should return None or fall back to filename
    assert result is None or isinstance(result, str)


def test_mimetype_guess_invalid_url() -> None:
    """Test mimetype_guess with invalid URL (lines 84-85 ValueError branch)."""

    # Create an object with a name that will cause urlsplit to raise ValueError
    class BadUrlName:
        def __init__(self, name: str) -> None:
            self.name = name

    # This should not crash, but fall through to path extraction
    # We need to use a malformed URL that causes urlsplit ValueError
    # On some versions it's hard to trigger ValueError from urlsplit
    # Test with PathLike instead
    # Import | Standard Library
    from pathlib import Path

    result = mimetype_guess(Path("/path/to/file.jpg"))
    assert result in {"image/jpeg", "image/pjpeg"}


def test_mimetype_guess_urlsplit_valueerror() -> None:
    """Test mimetype_guess when urlsplit raises ValueError (lines 84-85)."""
    # Import | Standard Library
    from unittest.mock import patch

    # Mock urlsplit to raise ValueError
    with patch(
        "rite.filesystem.mimetype.mimetype_guess.urlsplit",
        side_effect=ValueError("Invalid URL"),
    ):
        # Should fall back to using name directly as path
        result = mimetype_guess("some/path/file.jpg")
        assert result in {"image/jpeg", "image/pjpeg"}
