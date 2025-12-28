# =============================================================================
# Test: path_exists
# =============================================================================

"""
Tests for rite.filesystem.path.path_exists.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Local Modules
from rite.filesystem.path.path_exists import (
    path_exists,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_path_exists(tmp_path: Path) -> None:
    """Test path_exists() function."""
    # Create a test file
    test_file = tmp_path / "test.txt"
    test_file.write_text("test")

    # Test existing path
    assert path_exists(str(test_file)) is True
    assert path_exists(str(tmp_path)) is True

    # Test non-existing path
    assert path_exists(str(tmp_path / "nonexistent.txt")) is False
