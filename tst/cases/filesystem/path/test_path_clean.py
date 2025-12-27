# =============================================================================
# Test: path_clean
# =============================================================================

"""
Tests for rite.filesystem.path.path_clean.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.path.path_clean import (
    path_clean,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_path_clean() -> None:
    """Test path_clean() function."""
    # Test removing leading/trailing slashes
    assert path_clean("//path/to/file//") == "/path/to/file"
    assert path_clean("path/to/file") == "/path/to/file"

    # Test single slash
    assert path_clean("/") == "/"

    # Test multiple slashes (only leading/trailing stripped, not internal)
    assert path_clean("///a///b///") == "/a///b"
