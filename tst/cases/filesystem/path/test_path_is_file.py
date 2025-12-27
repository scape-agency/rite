# =============================================================================
# Test: path_is_file
# =============================================================================

"""
Tests for rite.filesystem.path.path_is_file.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.path.path_is_file import (
    path_is_file,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_path_is_file(tmp_path: Path) -> None:
    """Test path_is_file() function."""
    # Create test file and directory
    test_file = tmp_path / "test.txt"
    test_file.write_text("test")
    test_dir = tmp_path / "subdir"
    test_dir.mkdir()

    # Test file
    assert path_is_file(str(test_file)) is True

    # Test directory
    assert path_is_file(str(tmp_path)) is False
    assert path_is_file(str(test_dir)) is False

    # Test non-existing
    assert path_is_file(str(tmp_path / "nonexistent.txt")) is False
