# =============================================================================
# Test: mimetype_read_head_bytes
# =============================================================================

"""
Tests for rite.filesystem.mimetype.mimetype_read_head_bytes.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import io
from pathlib import Path

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.mimetype.mimetype_read_head_bytes import read_head_bytes

# =============================================================================
# Test Functions
# =============================================================================


def test_read_head_bytes_from_bytes_and_path(tmp_path: Path) -> None:
    """Test reading head bytes from raw bytes and a file path."""
    assert read_head_bytes(b"abcdef", n=3) == b"abc"

    path = tmp_path / "data.bin"
    path.write_bytes(b"xyz123")
    assert read_head_bytes(path, n=4) == b"xyz1"


def test_read_head_bytes_preserves_stream_position() -> None:
    """Test that reading from a stream does not consume it."""
    stream = io.BytesIO(b"abcdef")
    stream.read(2)

    head = read_head_bytes(stream, n=3)

    assert head == b"cde"
    assert stream.read() == b"cdef"
