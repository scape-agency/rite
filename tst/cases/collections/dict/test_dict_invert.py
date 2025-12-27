# =============================================================================
# Test: dict_invert
# =============================================================================

"""
Tests for rite.collections.dict.dict_invert.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.dict.dict_invert import (
    dict_invert,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_dict_invert() -> None:
    """Test dict_invert() function."""
    # Basic invert
    result = dict_invert({"a": 1, "b": 2, "c": 3})
    assert result == {1: "a", 2: "b", 3: "c"}

    # Empty dict
    result = dict_invert({})
    assert result == {}

    # String values
    result = dict_invert({"key1": "value1", "key2": "value2"})
    assert result == {"value1": "key1", "value2": "key2"}
