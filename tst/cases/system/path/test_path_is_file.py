# =============================================================================
# Test: path_is_file
# =============================================================================

"""
Tests for rite.system.path.path_is_file.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.path.path_is_file import (
    path_is_file,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_path_is_file(tmp_path) -> None:
    """Test path_is_file() function."""
    # Create a file and directory for testing
    test_file = tmp_path / "test.txt"
    test_file.write_text("test")
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()

    # Test file
    assert path_is_file(str(test_file)) is True

    # Test directory
    assert path_is_file(str(test_dir)) is False

    # Test non-existing path
    assert path_is_file(str(tmp_path / "nonexistent")) is False
