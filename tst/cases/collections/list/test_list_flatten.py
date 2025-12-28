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


def test_list_flatten_depth_zero() -> None:
    """Test list_flatten with depth=0 returns original structure."""
    items = [[1, 2], [3, [4, 5]]]
    result = list_flatten(items, depth=0)
    assert result == [[1, 2], [3, [4, 5]]]


def test_list_flatten_depth_one() -> None:
    """Test list_flatten with depth=1 flattens one level."""
    items = [[1, [2, 3]], [4, [5, 6]]]
    result = list_flatten(items, depth=1)
    assert result == [1, [2, 3], 4, [5, 6]]


def test_list_flatten_depth_two() -> None:
    """Test list_flatten with depth=2 flattens two levels."""
    items = [[[1, 2], 3], [4, [5, [6, 7]]]]
    result = list_flatten(items, depth=2)
    assert result == [1, 2, 3, 4, 5, [6, 7]]


def test_list_flatten_mixed_types() -> None:
    """Test list_flatten with mixed types."""
    items = [[1, "a"], [2, "b"], ["c", [3, 4]]]
    result = list_flatten(items)
    assert result == [1, "a", 2, "b", "c", 3, 4]


def test_list_flatten_deeply_nested() -> None:
    """Test list_flatten with deeply nested lists."""
    items = [[[[[1]]]]]
    result = list_flatten(items)
    assert result == [1]


def test_list_flatten_with_non_list_items() -> None:
    """Test list_flatten with non-list items at various levels."""
    items = [1, [2, 3], 4, [[5, 6], 7], 8]
    result = list_flatten(items)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8]


def test_list_flatten_empty_nested_lists() -> None:
    """Test list_flatten with multiple empty lists."""
    items = [[], [[]], [[[]]], [1, [], 2]]
    result = list_flatten(items)
    assert result == [1, 2]


def test_list_flatten_depth_exceeds_nesting() -> None:
    """Test list_flatten when depth exceeds actual nesting."""
    items = [[1, 2], [3, 4]]
    result = list_flatten(items, depth=10)
    assert result == [1, 2, 3, 4]


def test_list_flatten_preserves_non_list_structure() -> None:
    """Test that non-list items are preserved without modification."""

    class CustomObj:
        def __init__(self, val: int) -> None:
            self.val = val

    obj = CustomObj(42)
    items = [[obj, 1], [2, [3, obj]]]
    result = list_flatten(items)
    assert len(result) == 5
    assert result[0] is obj
    assert result[4] is obj
