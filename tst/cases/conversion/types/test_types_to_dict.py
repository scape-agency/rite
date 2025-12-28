# =============================================================================
# Test: types_to_dict
# =============================================================================

"""
Tests for rite.conversion.types.types_to_dict.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from collections.abc import Mapping

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.types.types_to_dict import (
    types_to_dict,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_types_to_dict_from_mapping_and_pairs() -> None:
    """Test conversion from mappings and sequences of key/value pairs."""
    data = {"a": 1, "b": 2}
    assert types_to_dict(data) is data

    # Test with non-dict Mapping to exercise the Mapping branch
    class CustomMapping(Mapping):
        """Custom mapping that doesn't inherit from dict."""

        def __init__(self, data: dict) -> None:
            self._data = data

        def __getitem__(self, key):
            return self._data[key]

        def __iter__(self):
            return iter(self._data)

        def __len__(self):
            return len(self._data)

    custom = CustomMapping({"x": 10, "y": 20})
    result = types_to_dict(custom)
    assert result == {"x": 10, "y": 20}

    pairs = [("a", 1), ("b", 2)]
    assert types_to_dict(pairs) == {"a": 1, "b": 2}


def test_types_to_dict_with_key_attr() -> None:
    """Test using key_attr to build dict from objects."""

    class Item:
        def __init__(self, key: str, value: int) -> None:
            self.key = key
            self.value = value

    items = [Item("a", 1), Item("b", 2)]
    result = types_to_dict(items, key_attr="key")
    assert set(result.keys()) == {"a", "b"}
    assert result["a"].value == 1
    assert result["b"].value == 2


def test_types_to_dict_with_key_attr_missing() -> None:
    """Test key_attr when some items don't have the attribute (line 79)."""

    class Item:
        def __init__(self, key: str) -> None:
            self.key = key

    class NoKey:
        pass

    items = [Item("a"), NoKey(), Item("b")]
    result = types_to_dict(items, key_attr="key")
    # Only items with 'key' attr should be in result
    assert set(result.keys()) == {"a", "b"}


def test_types_to_dict_list_not_pairs() -> None:
    """Test list that isn't key-value pairs (line 76->84)."""
    # List of single items, not pairs - should fail
    with pytest.raises(ValueError):
        types_to_dict([1, 2, 3])


def test_types_to_dict_invalid_input_raises() -> None:
    """Test that unsupported inputs raise ValueError."""
    with pytest.raises(ValueError):
        types_to_dict(123)
