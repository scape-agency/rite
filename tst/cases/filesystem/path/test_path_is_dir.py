# =============================================================================
# Test: path_is_dir
# =============================================================================

"""
Tests for rite.filesystem.path.path_is_dir.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.path.path_is_dir import (
    path_is_dir,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_path_is_dir(tmp_path: Path) -> None:
    """Test path_is_dir() function."""
    # Create test file and directory
    test_file = tmp_path / "test.txt"
    test_file.write_text("test")
    test_dir = tmp_path / "subdir"
    test_dir.mkdir()

    # Test directory
    assert path_is_dir(str(tmp_path)) is True
    assert path_is_dir(str(test_dir)) is True

    # Test file
    assert path_is_dir(str(test_file)) is False

    # Test non-existing
    assert path_is_dir(str(tmp_path / "nonexistent")) is False
