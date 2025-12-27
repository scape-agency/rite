# =============================================================================
# Test: list_unique
# =============================================================================

"""
Tests for rite.collections.list.list_unique.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.list.list_unique import (
    list_unique,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "items,expected",
    [
        ([1, 2, 2, 3, 3, 3], [1, 2, 3]),
        (["a", "b", "a", "c"], ["a", "b", "c"]),
        ([], []),
        ([1], [1]),
        ([1, 1, 1], [1]),
    ],
)
def test_list_unique(items: list, expected: list) -> None:
    """Test list_unique() with various inputs."""
    assert list_unique(items) == expected
