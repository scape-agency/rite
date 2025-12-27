# =============================================================================
# Test: path_exists
# =============================================================================

"""
Tests for rite.system.path.path_exists.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.path.path_exists import (
    path_exists,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_path_exists(tmp_path) -> None:
    """Test path_exists() function."""
    # Create a file and directory for testing
    test_file = tmp_path / "test.txt"
    test_file.write_text("test")
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()

    # Test existing file
    assert path_exists(str(test_file)) is True

    # Test existing directory
    assert path_exists(str(test_dir)) is True

    # Test non-existing path
    assert path_exists(str(tmp_path / "nonexistent")) is False
