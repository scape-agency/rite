# =============================================================================
# Test: path_join
# =============================================================================

"""
Tests for rite.system.path.path_join.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.system.path.path_join import (
    path_join,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "parts,expected",
    [
        (("path", "to", "file.txt"), "path/to/file.txt"),
        (("dir",), "dir"),
        (("path", ""), "path"),
    ],
)
def test_path_join(parts, expected) -> None:
    """Test path_join() with various parts."""
    result = path_join(*parts)
    # Normalize path separators for cross-platform comparison
    assert result.replace("\\", "/") == expected.replace("\\", "/")
