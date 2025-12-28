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
        instance = _TotalSize(1024)
        assert instance is not None
        assert instance.size == 1024

    def test_tell(self) -> None:
        """Test _TotalSize.tell() method."""
        instance = _TotalSize(2048)
        assert instance.tell() == 2048

    def test_seek(self) -> None:
        """Test _TotalSize.seek() method."""
        instance = _TotalSize(4096)
        assert instance.seek() == 4096


# =============================================================================
# Test Functions
# =============================================================================


def test_folder_size_to_string() -> None:
    """Test folder_size_to_string() function."""
    # TODO: Implement test
    # result = folder_size_to_string(test_input)
    # assert result == expected_output
    pytest.skip("Test not implemented")
