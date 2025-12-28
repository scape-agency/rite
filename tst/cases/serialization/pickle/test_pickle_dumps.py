# =============================================================================
# Test: pickle_dumps
# =============================================================================

"""
Tests for rite.serialization.pickle.pickle_dumps.
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
from rite.serialization.pickle.pickle_dumps import (
    pickle_dumps,
)

# =============================================================================
# Test Classes
# =============================================================================


class TestPickleDumps:
    """Tests for pickle_dumps() function."""

    def test_dumps_dict_to_bytes(self) -> None:
        """Test converting a dictionary to bytes."""
        test_data = {"key": "value", "number": 42}
        result = pickle_dumps(test_data)

        # Verify result is bytes
        assert isinstance(result, bytes)

        # Verify the data can be deserialized correctly
        loaded_data = pickle.loads(result)
        assert loaded_data == test_data

    def test_dumps_list_to_bytes(self) -> None:
        """Test converting a list to bytes."""
        test_data = [1, 2, 3, 4, 5]
        result = pickle_dumps(test_data)

        # Verify result is bytes
        assert isinstance(result, bytes)

        # Verify the data can be deserialized correctly
        loaded_data = pickle.loads(result)
        assert loaded_data == test_data

    def test_dumps_string_to_bytes(self) -> None:
        """Test converting a string to bytes."""
        test_data = "Hello, World!"
        result = pickle_dumps(test_data)

        # Verify result is bytes
        assert isinstance(result, bytes)

        # Verify the data can be deserialized correctly
        loaded_data = pickle.loads(result)
        assert loaded_data == test_data

    def test_dumps_nested_structure(self) -> None:
        """Test dumping complex nested data structures."""
        test_data = {
            "users": [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
            ],
            "counts": [1, 2, 3],
            "active": True,
        }

        result = pickle_dumps(test_data)

        # Verify result is bytes
        assert isinstance(result, bytes)

        # Verify the data can be deserialized correctly
        loaded_data = pickle.loads(result)
        assert loaded_data == test_data

    def test_dumps_none_value(self) -> None:
        """Test dumping None value to bytes."""
        test_data = None
        result = pickle_dumps(test_data)

        # Verify result is bytes
        assert isinstance(result, bytes)

        # Verify the data can be deserialized correctly
        loaded_data = pickle.loads(result)
        assert loaded_data is None

    def test_dumps_boolean_values(self) -> None:
        """Test dumping boolean values to bytes."""
        test_data = {"true": True, "false": False}
        result = pickle_dumps(test_data)

        # Verify result is bytes
        assert isinstance(result, bytes)

        # Verify the data can be deserialized correctly
        loaded_data = pickle.loads(result)
        assert loaded_data == test_data

    def test_dumps_numeric_types(self) -> None:
        """Test dumping various numeric types."""
        test_data = {
            "integer": 42,
            "float": 3.14,
            "negative": -10,
            "zero": 0,
        }

        result = pickle_dumps(test_data)

        # Verify result is bytes
        assert isinstance(result, bytes)

        # Verify the data can be deserialized correctly
        loaded_data = pickle.loads(result)
        assert loaded_data == test_data

    def test_dumps_tuple_and_set(self) -> None:
        """Test dumping tuples and sets."""
        test_data = {"tuple": (1, 2, 3), "set": {4, 5, 6}}

        result = pickle_dumps(test_data)

        # Verify result is bytes
        assert isinstance(result, bytes)

        # Verify the data can be deserialized correctly
        loaded_data = pickle.loads(result)
        assert loaded_data == test_data

    def test_dumps_empty_collections(self) -> None:
        """Test dumping empty collections."""
        test_data = {"empty_list": [], "empty_dict": {}, "empty_set": set()}

        result = pickle_dumps(test_data)

        # Verify result is bytes
        assert isinstance(result, bytes)

        # Verify the data can be deserialized correctly
        loaded_data = pickle.loads(result)
        assert loaded_data == test_data

    def test_dumps_result_is_not_empty(self) -> None:
        """Test that dumps result is not empty."""
        test_data = {"key": "value"}
        result = pickle_dumps(test_data)

        # Verify result is not empty
        assert len(result) > 0

    def test_dumps_returns_bytes_type(self) -> None:
        """Test that dumps always returns bytes type."""
        test_cases = [
            {"dict": "data"},
            [1, 2, 3],
            "string",
            42,
            3.14,
            True,
            None,
        ]

        for test_data in test_cases:
            result = pickle_dumps(test_data)
            assert isinstance(result, bytes)

    def test_dumps_roundtrip_consistency(self) -> None:
        """Test that dumps/loads round-trip is consistent."""
        test_data = {
            "name": "Test",
            "values": [1, 2, 3],
            "nested": {"key": "value"},
        }

        # Serialize and deserialize
        serialized = pickle_dumps(test_data)
        deserialized = pickle.loads(serialized)

        # Verify round-trip consistency
        assert deserialized == test_data

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
    def test_dumps_various_types(self, test_data) -> None:
        """Test dumping various data types to bytes."""
        result = pickle_dumps(test_data)

        # Verify result is bytes
        assert isinstance(result, bytes)

        # Verify the data can be deserialized correctly
        loaded_data = pickle.loads(result)
        assert loaded_data == test_data
