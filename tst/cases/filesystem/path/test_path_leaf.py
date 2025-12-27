# =============================================================================
# Test: path_leaf
# =============================================================================

"""
Tests for rite.filesystem.path.path_leaf.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.path.path_leaf import (
    path_leaf,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_path_leaf() -> None:
    """Test path_leaf() function."""
    # Test basic leaf extraction
    assert path_leaf("/a/b/c/file.txt") == "file.txt"
    assert path_leaf("/a/b/c/folder") == "folder"
    assert path_leaf("file.txt") == "file.txt"

    # Test with trailing slash
    assert path_leaf("/a/b/c/") in ["", "c"]  # May vary by OS
