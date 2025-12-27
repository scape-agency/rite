# =============================================================================
# Test: dict_filter
# =============================================================================

"""
Tests for rite.collections.dict.dict_filter.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.dict.dict_filter import (
    dict_filter,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_dict_filter() -> None:
    """Test dict_filter() function."""
    # Filter by value
    result = dict_filter({"a": 1, "b": 2, "c": 3}, lambda k, v: v > 1)
    assert result == {"b": 2, "c": 3}

    # Filter by key
    result = dict_filter({"a": 1, "b": 2, "c": 3}, lambda k, v: k != "b")
    assert result == {"a": 1, "c": 3}

    # Filter all out
    result = dict_filter({"a": 1, "b": 2}, lambda k, v: False)
    assert result == {}
