# =============================================================================
# Test: file_size_to_string
# =============================================================================

"""
Tests for rite.filesystem.file.file_size_to_string.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Standard Library
from io import BytesIO

# Import | Local Modules
from rite.filesystem.file.file_size_to_string import (
    _SizedStream,
    file_size_to_string,
)

# =============================================================================
# Test Class: _SizedStream
# =============================================================================


class Test_SizedStream:
    """Tests for _SizedStream class."""

    def test_instantiation(self) -> None:
        """Test _SizedStream can be instantiated."""
        # _SizedStream is a Protocol, not meant to be instantiated directly
        # Just verify the protocol exists
        assert _SizedStream is not None

    def test_tell(self) -> None:
        """Test _SizedStream.tell() method."""
        # Test with BytesIO which implements the protocol
        stream = BytesIO(b"test")
        assert stream.tell() == 0
        stream.read(2)
        assert stream.tell() == 2

    def test_seek(self) -> None:
        """Test _SizedStream.seek() method."""
        # Test with BytesIO which implements the protocol
        stream = BytesIO(b"test")
        stream.seek(2)
        assert stream.tell() == 2


# =============================================================================
# Test Functions
# =============================================================================


def test_file_size_to_string() -> None:
    """Test file_size_to_string() function."""
    # Test with BytesIO
    stream = BytesIO(b"a" * 1024)
    result = file_size_to_string(stream)
    assert result == "1.00 KB"

    # Test with small file
    small_stream = BytesIO(b"a" * 100)
    result = file_size_to_string(small_stream)
    assert result == "100 B"

    # Test with object having size attribute
    class SizedFile:
        def __init__(self, size: int) -> None:
            self.size = size

        def tell(self) -> int:
            return 0

        def seek(self, pos: int, whence: int = 0) -> int:
            return 0

    sized = SizedFile(2048)
    result = file_size_to_string(sized)  # type: ignore
    assert result == "2.00 KB"
