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
