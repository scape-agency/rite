# =============================================================================
# Test: pickle_loads
# =============================================================================

"""
Tests for rite.serialization.pickle.pickle_loads.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import pickle

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.pickle.pickle_loads import (
    pickle_loads,
)

# =============================================================================
# Test Classes
# =============================================================================


class TestPickleLoads:
    """Tests for pickle_loads() function."""

    def test_loads_dict_from_bytes(self) -> None:
        """Test loading a dictionary from bytes."""
        test_data = {"key": "value", "number": 42}
        serialized = pickle.dumps(test_data)

        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result == test_data

    def test_loads_list_from_bytes(self) -> None:
        """Test loading a list from bytes."""
        test_data = [1, 2, 3, 4, 5]
        serialized = pickle.dumps(test_data)

        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result == test_data

    def test_loads_string_from_bytes(self) -> None:
        """Test loading a string from bytes."""
        test_data = "Hello, World!"
        serialized = pickle.dumps(test_data)

        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result == test_data

    def test_loads_nested_structure(self) -> None:
        """Test loading complex nested data structures."""
        test_data = {
            "users": [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
            ],
            "counts": [1, 2, 3],
            "active": True,
        }
        serialized = pickle.dumps(test_data)

        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result == test_data

    def test_loads_none_value(self) -> None:
        """Test loading None value from bytes."""
        test_data = None
        serialized = pickle.dumps(test_data)

        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result is None

    def test_loads_boolean_values(self) -> None:
        """Test loading boolean values from bytes."""
        test_data = {"true": True, "false": False}
        serialized = pickle.dumps(test_data)

        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result == test_data

    def test_loads_numeric_types(self) -> None:
        """Test loading various numeric types."""
        test_data = {
            "integer": 42,
            "float": 3.14,
            "negative": -10,
            "zero": 0,
        }
        serialized = pickle.dumps(test_data)

        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result == test_data

    def test_loads_tuple_and_set(self) -> None:
        """Test loading tuples and sets."""
        test_data = {"tuple": (1, 2, 3), "set": {4, 5, 6}}
        serialized = pickle.dumps(test_data)

        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result == test_data

    def test_loads_empty_collections(self) -> None:
        """Test loading empty collections."""
        test_data = {"empty_list": [], "empty_dict": {}, "empty_set": set()}
        serialized = pickle.dumps(test_data)

        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result == test_data

    def test_loads_large_data(self) -> None:
        """Test loading large data structures."""
        test_data = {
            "items": list(range(10000)),
            "nested": {i: i**2 for i in range(100)},
        }
        serialized = pickle.dumps(test_data)

        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result == test_data
        assert len(result["items"]) == 10000

    def test_loads_empty_dict(self) -> None:
        """Test loading an empty dictionary."""
        test_data = {}
        serialized = pickle.dumps(test_data)

        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result == {}

    def test_loads_empty_list(self) -> None:
        """Test loading an empty list."""
        test_data = []
        serialized = pickle.dumps(test_data)

        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result == []

    def test_loads_roundtrip_consistency(self) -> None:
        """Test that loads is consistent with dumps."""
        test_data = {
            "name": "Test",
            "values": [1, 2, 3],
            "nested": {"key": "value"},
        }

        # Serialize and deserialize
        serialized = pickle.dumps(test_data)
        deserialized = pickle_loads(serialized)

        # Verify round-trip consistency
        assert deserialized == test_data

    def test_loads_unicode_strings(self) -> None:
        """Test loading unicode strings."""
        test_data = {"emoji": "😀🎉", "chinese": "你好", "arabic": "مرحبا"}
        serialized = pickle.dumps(test_data)

        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result == test_data

    def test_loads_deep_nesting(self) -> None:
        """Test loading deeply nested structures."""
        test_data = {"level1": {"level2": {"level3": {"level4": "deep"}}}}
        serialized = pickle.dumps(test_data)

        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result == test_data

    @pytest.mark.parametrize(
        "test_data",
        [
            {"single": "item"},
            [42],
            "text",
            123,
            3.14,
            True,
            False,
            None,
            [],
            {},
        ],
    )
    def test_loads_various_types(self, test_data) -> None:
        """Test loading various data types from bytes."""
        serialized = pickle.dumps(test_data)
        result = pickle_loads(serialized)

        # Verify the loaded data
        assert result == test_data

    def test_loads_bytes_type_required(self) -> None:
        """Test that loads expects bytes input."""
        test_data = {"key": "value"}
        serialized = pickle.dumps(test_data)

        # Should work with bytes
        result = pickle_loads(serialized)
        assert result == test_data
