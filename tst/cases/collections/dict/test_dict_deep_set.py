# =============================================================================
# Test: dict_deep_set
# =============================================================================

"""
Tests for rite.collections.dict.dict_deep_set.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.dict.dict_deep_set import (
    dict_deep_set,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_dict_deep_set() -> None:
    """Test dict_deep_set() function."""
    # Create nested structure
    d1: dict[str, dict] = {}
    dict_deep_set(d1, ["user", "profile", "name"], "John")
    assert d1 == {"user": {"profile": {"name": "John"}}}

    # Update existing nested value
    d2 = {"user": {"profile": {"name": "Jane"}}}
    dict_deep_set(d2, ["user", "profile", "name"], "John")
    assert d2 == {"user": {"profile": {"name": "John"}}}

    # Add to existing structure
    d3 = {"user": {"profile": {"name": "John"}}}
    dict_deep_set(d3, ["user", "profile", "age"], 30)
    assert d3 == {"user": {"profile": {"name": "John", "age": 30}}}
