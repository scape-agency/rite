# =============================================================================
# Test: dict_deep_get
# =============================================================================

"""
Tests for rite.collections.dict.dict_deep_get.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.dict.dict_deep_get import (
    dict_deep_get,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_dict_deep_get() -> None:
    """Test dict_deep_get() function."""
    # Nested get
    data = {"user": {"profile": {"name": "John", "age": 30}}}
    result = dict_deep_get(data, ["user", "profile", "name"])
    assert result == "John"

    # Single level
    result = dict_deep_get({"a": 1}, ["a"])
    assert result == 1

    # Default value for missing key
    result = dict_deep_get(data, ["user", "missing"], default="N/A")
    assert result == "N/A"
