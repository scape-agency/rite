# =============================================================================
# Test: list_chunk
# =============================================================================

"""
Tests for rite.collections.list.list_chunk.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.list.list_chunk import (
    list_chunk,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "items,size,expected",
    [
        ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
        ([1, 2, 3, 4, 5, 6], 3, [[1, 2, 3], [4, 5, 6]]),
        ([], 2, []),
        ([1], 2, [[1]]),
        ([1, 2], 1, [[1], [2]]),
    ],
)
def test_list_chunk(
    items: list[int], size: int, expected: list[list[int]]
) -> None:
    """Test list_chunk() with various inputs."""
    assert list_chunk(items, size) == expected
