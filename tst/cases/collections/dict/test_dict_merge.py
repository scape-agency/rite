# =============================================================================
# Test: dict_merge
# =============================================================================

"""
Tests for rite.collections.dict.dict_merge.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.dict.dict_merge import (
    dict_merge,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_dict_merge() -> None:
    """Test dict_merge() function."""
    # Test basic merge
    result = dict_merge({"a": 1, "b": 2}, {"b": 3, "c": 4})
    assert result == {"a": 1, "b": 3, "c": 4}

    # Test merging multiple dicts
    result = dict_merge({"a": 1}, {"b": 2}, {"c": 3})
    assert result == {"a": 1, "b": 2, "c": 3}

    # Test with empty dict
    result = dict_merge({"a": 1}, {})
    assert result == {"a": 1}

    # Test no arguments
    result = dict_merge()
    assert result == {}

    # Test single dict
    result = dict_merge({"a": 1, "b": 2})
    assert result == {"a": 1, "b": 2}

    # Test complete override
    result = dict_merge({"a": 1, "b": 2}, {"a": 10, "b": 20})
    assert result == {"a": 10, "b": 20}

    # Test mixed types
    result = dict_merge({"a": 1, "b": "text"}, {"c": 3.14})
    assert result == {"a": 1, "b": "text", "c": 3.14}


def test_dict_merge_deep() -> None:
    """Test dict_merge() with deep=True."""
    # Test deep merge of nested dicts
    d1 = {"a": {"x": 1}}
    d2 = {"a": {"y": 2}}
    result = dict_merge(d1, d2, deep=True)
    assert result == {"a": {"x": 1, "y": 2}}

    # Test deep merge with multiple levels
    d1 = {"a": {"b": {"x": 1}}}
    d2 = {"a": {"b": {"y": 2}}}
    result = dict_merge(d1, d2, deep=True)
    assert result == {"a": {"b": {"x": 1, "y": 2}}}

    # Test deep merge overriding nested values
    d1 = {"a": {"x": 1}}
    d2 = {"a": {"x": 10}}
    result = dict_merge(d1, d2, deep=True)
    assert result == {"a": {"x": 10}}

    # Test deep merge when value is not a dict
    d1 = {"a": {"x": 1}}
    d2 = {"a": "string"}
    result = dict_merge(d1, d2, deep=True)
    assert result == {"a": "string"}

    # Test deep merge of three dicts
    d1 = {"a": {"x": 1}}
    d2 = {"a": {"y": 2}}
    d3 = {"a": {"z": 3}}
    result = dict_merge(d1, d2, d3, deep=True)
    assert result == {"a": {"x": 1, "y": 2, "z": 3}}

    # Test deep merge with empty nested dicts
    d1 = {"a": {}}
    d2 = {"a": {"x": 1}}
    result = dict_merge(d1, d2, deep=True)
    assert result == {"a": {"x": 1}}

    # Test deep merge adding new keys
    d1 = {"a": {"x": 1}, "b": 2}
    d2 = {"a": {"y": 2}, "c": 3}
    result = dict_merge(d1, d2, deep=True)
    assert result == {"a": {"x": 1, "y": 2}, "b": 2, "c": 3}

    # Test shallow vs deep merge
    d1 = {"a": {"x": 1}}
    d2 = {"a": {"y": 2}}
    shallow = dict_merge(d1, d2, deep=False)
    deep = dict_merge(d1, d2, deep=True)
    assert shallow == {"a": {"y": 2}}
    assert deep == {"a": {"x": 1, "y": 2}}


def test_dict_merge_edge_cases() -> None:
    """Test dict_merge() edge cases."""
    # Test with None values
    result = dict_merge({"a": 1, "b": None}, {"b": 2})
    assert result == {"a": 1, "b": 2}

    # Test with zero values
    result = dict_merge({"a": 0}, {"a": 1})
    assert result == {"a": 1}

    # Test with False values
    result = dict_merge({"a": False}, {"a": True})
    assert result == {"a": True}

    # Test large dicts
    d1 = {f"key_{i}": i for i in range(500)}
    d2 = {f"key_{i}": i * 2 for i in range(250, 750)}
    result = dict_merge(d1, d2)
    assert len(result) == 750
    assert result[f"key_100"] == 100
    assert result[f"key_600"] == 1200
