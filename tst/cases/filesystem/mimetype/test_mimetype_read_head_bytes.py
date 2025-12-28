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


def test_read_head_bytes_from_bytearray() -> None:
    """Test reading head bytes from bytearray."""
    data = bytearray(b"hello world")
    assert read_head_bytes(data, n=5) == b"hello"


def test_read_head_bytes_from_memoryview() -> None:
    """Test reading head bytes from memoryview."""
    data = memoryview(b"test data")
    assert read_head_bytes(data, n=4) == b"test"


def test_read_head_bytes_from_string_path(tmp_path: Path) -> None:
    """Test reading head bytes from string path."""
    path = tmp_path / "test.txt"
    path.write_bytes(b"content here")
    assert read_head_bytes(str(path), n=7) == b"content"


def test_read_head_bytes_nonexistent_path() -> None:
    """Test reading from nonexistent path returns None."""
    result = read_head_bytes("/nonexistent/path/file.bin", n=10)
    assert result is None


def test_read_head_bytes_with_peek() -> None:
    """Test reading from stream with peek method."""
    stream = io.BufferedReader(io.BytesIO(b"peek data"))
    result = read_head_bytes(stream, n=4)
    assert result == b"peek"


def test_read_head_bytes_non_seekable_stream() -> None:
    """Test reading from non-seekable stream returns None."""

    class NonSeekableStream:
        def read(self, n: int) -> bytes:
            return b"data"

    stream = NonSeekableStream()
    result = read_head_bytes(stream, n=4)
    assert result is None


def test_read_head_bytes_no_read_method() -> None:
    """Test object without read method returns None."""

    class NotAStream:
        pass

    result = read_head_bytes(NotAStream(), n=10)
    assert result is None


def test_read_head_bytes_oserror_on_path(tmp_path: Path) -> None:
    """Test OSError when reading from path returns None."""
    # Create a directory - reading from directory causes OSError
    dir_path = tmp_path / "mydir"
    dir_path.mkdir()
    result = read_head_bytes(dir_path, n=10)
    assert result is None


def test_read_head_bytes_short_data() -> None:
    """Test reading more bytes than available."""
    assert read_head_bytes(b"ab", n=10) == b"ab"


def test_read_head_bytes_oserror_on_tell(tmp_path: Path) -> None:
    """Test OSError during tell/seek returns None."""

    class FailingStream:
        def read(self, n: int) -> bytes:
            return b"data"

        def tell(self) -> int:
            raise OSError("Cannot tell")

        def seek(self, pos: int, whence: int = 0) -> int:
            raise OSError("Cannot seek")

    stream = FailingStream()
    result = read_head_bytes(stream, n=4)
    assert result is None


def test_read_head_bytes_failing_peek() -> None:
    """Test stream with failing peek falls through to read/seek."""

    class FailingPeekStream:
        def peek(self, n: int) -> bytes:
            raise OSError("Peek failed")

        def read(self, n: int) -> bytes:
            return b"fallback"[:n]

        def tell(self) -> int:
            return 0

        def seek(self, pos: int, whence: int = 0) -> int:
            return 0

    stream = FailingPeekStream()
    result = read_head_bytes(stream, n=4)
    assert result == b"fall"
