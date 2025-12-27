# =============================================================================
# Test: list_group_by
# =============================================================================

"""
Tests for rite.collections.list.list_group_by.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.list.list_group_by import (
    list_group_by,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_list_group_by() -> None:
    """Test list_group_by() with various key functions."""
    # Test with attribute key
    data = [
        {"type": "fruit", "name": "apple"},
        {"type": "vegetable", "name": "carrot"},
        {"type": "fruit", "name": "banana"},
    ]
    result = list_group_by(data, key="type")
    assert "fruit" in result
    assert "vegetable" in result
    assert len(result["fruit"]) == 2
    assert len(result["vegetable"]) == 1

    # Test with function key
    numbers = [1, 2, 3, 4, 5, 6]
    result = list_group_by(numbers, key=lambda x: x % 2)
    assert len(result[0]) == 3  # Even numbers
    assert len(result[1]) == 3  # Odd numbers
