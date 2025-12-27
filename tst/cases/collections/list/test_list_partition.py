# =============================================================================
# Test: list_partition
# =============================================================================

"""
Tests for rite.collections.list.list_partition.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.list.list_partition import (
    list_partition,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_list_partition() -> None:
    """Test list_partition() with various predicates."""
    # Test with even/odd predicate
    result = list_partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
    assert result == ([2, 4], [1, 3, 5])

    # Test with string length
    result = list_partition(["a", "ab", "abc"], lambda x: len(x) > 1)
    assert result == (["ab", "abc"], ["a"])

    # Test with all matching
    result = list_partition([2, 4, 6], lambda x: x % 2 == 0)
    assert result == ([2, 4, 6], [])

    # Test with none matching
    result = list_partition([1, 3, 5], lambda x: x % 2 == 0)
    assert result == ([], [1, 3, 5])
