# =============================================================================
# Test: folder_size_to_string
# =============================================================================

"""
Tests for rite.filesystem.folder.folder_size_to_string.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.folder.folder_size_to_string import (
    _TotalSize,
    folder_size_to_string,
)

# =============================================================================
# Test Class: _TotalSize
# =============================================================================


class Test_TotalSize:
    """Tests for _TotalSize class."""

    def test_instantiation(self) -> None:
        """Test _TotalSize can be instantiated."""
        # TODO: Implement test
        instance = _TotalSize()
        assert instance is not None

    def test_tell(self) -> None:
        """Test _TotalSize.tell() method."""
        # TODO: Implement test
        instance = _TotalSize()
        # result = instance.tell()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_seek(self) -> None:
        """Test _TotalSize.seek() method."""
        # TODO: Implement test
        instance = _TotalSize()
        # result = instance.seek()
        # assert result is not None
        pytest.skip("Test not implemented")


# =============================================================================
# Test Functions
# =============================================================================


def test_folder_size_to_string() -> None:
    """Test folder_size_to_string() function."""
    # TODO: Implement test
    # result = folder_size_to_string(test_input)
    # assert result == expected_output
    pytest.skip("Test not implemented")
