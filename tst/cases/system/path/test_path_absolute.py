# =============================================================================
# Test: path_absolute
# =============================================================================

"""
Tests for rite.system.path.path_absolute.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.path.path_absolute import (
    path_absolute,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_path_absolute() -> None:
    """Test path_absolute() function."""
    # Import | Standard Library
    import os

    # Test relative path
    result = path_absolute("file.txt")
    assert os.path.isabs(result)

    # Test absolute path (should return as-is)
    abs_path = "/tmp/test.txt"
    result = path_absolute(abs_path)
    assert os.path.isabs(result)
