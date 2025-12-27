# =============================================================================
# Test: list_flatten
# =============================================================================

"""
Tests for rite.collections.list.list_flatten.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.list.list_flatten import (
    list_flatten,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "items,expected",
    [
        ([[1, 2], [3, 4], [5]], [1, 2, 3, 4, 5]),
        ([[1, [2, 3]], [4, 5]], [1, 2, 3, 4, 5]),
        ([], []),
        ([[1]], [1]),
        ([[], [2, 3], []], [2, 3]),
    ],
)
def test_list_flatten(items: list[list[int]], expected: list[int]) -> None:
    """Test list_flatten() with various inputs."""
    assert list_flatten(items) == expected
