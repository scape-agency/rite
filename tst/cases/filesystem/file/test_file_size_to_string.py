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

# Import | Standard Library
import pytest

# Import | Local Modules
from rite.filesystem.file.file_size_to_string import (
    file_size_to_string,
    _SizedStream,
)


# =============================================================================
# Test Class: _SizedStream
# =============================================================================


class Test_SizedStream:
    """Tests for _SizedStream class."""

    def test_instantiation(self) -> None:
        """Test _SizedStream can be instantiated."""
        # TODO: Implement test
        instance = _SizedStream()
        assert instance is not None

    def test_tell(self) -> None:
        """Test _SizedStream.tell() method."""
        # TODO: Implement test
        instance = _SizedStream()
        # result = instance.tell()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_seek(self) -> None:
        """Test _SizedStream.seek() method."""
        # TODO: Implement test
        instance = _SizedStream()
        # result = instance.seek()
        # assert result is not None
        pytest.skip("Test not implemented")


# =============================================================================
# Test Functions
# =============================================================================


def test_file_size_to_string() -> None:
    """Test file_size_to_string() function."""
    # TODO: Implement test
    # result = file_size_to_string(test_input)
    # assert result == expected_output
    pytest.skip("Test not implemented")

