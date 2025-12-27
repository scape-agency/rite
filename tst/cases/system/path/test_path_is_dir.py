# =============================================================================
# Test: path_is_dir
# =============================================================================

"""
Tests for rite.system.path.path_is_dir.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.path.path_is_dir import (
    path_is_dir,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_path_is_dir(tmp_path) -> None:
    """Test path_is_dir() function."""
    # Create a directory and file for testing
    test_file = tmp_path / "test.txt"
    test_file.write_text("test")
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()

    # Test directory
    assert path_is_dir(str(test_dir)) is True

    # Test file
    assert path_is_dir(str(test_file)) is False

    # Test non-existing path
    assert path_is_dir(str(tmp_path / "nonexistent")) is False
