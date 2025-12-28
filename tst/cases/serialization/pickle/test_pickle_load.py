# =============================================================================
# Test: pickle_load
# =============================================================================

"""
Tests for rite.serialization.pickle.pickle_load.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path
import pickle

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.pickle.pickle_load import (
    pickle_load,
)

# =============================================================================
# Test Classes
# =============================================================================


class TestPickleLoad:
    """Tests for pickle_load() function."""

    def test_load_dict_from_file(self, tmp_path: Path) -> None:
        """Test loading a dictionary from a pickle file."""
        file_path = tmp_path / "data.pkl"
        test_data = {"key": "value", "number": 42}

        # Create a pickle file
        with file_path.open("wb") as f:
            pickle.dump(test_data, f)

        # Load the file
        result = pickle_load(str(file_path))

        # Verify the loaded data
        assert result == test_data

    def test_load_list_from_file(self, tmp_path: Path) -> None:
        """Test loading a list from a pickle file."""
        file_path = tmp_path / "list_data.pkl"
        test_data = [1, 2, 3, 4, 5]

        # Create a pickle file
        with file_path.open("wb") as f:
            pickle.dump(test_data, f)

        # Load the file
        result = pickle_load(file_path)

        # Verify the loaded data
        assert result == test_data

    def test_load_string_from_file(self, tmp_path: Path) -> None:
        """Test loading a string from a pickle file."""
        file_path = tmp_path / "string_data.pkl"
        test_data = "Hello, World!"

        # Create a pickle file
        with file_path.open("wb") as f:
            pickle.dump(test_data, f)

        # Load the file
        result = pickle_load(file_path)

        # Verify the loaded data
        assert result == test_data

    def test_load_nested_structure(self, tmp_path: Path) -> None:
        """Test loading complex nested data structures."""
        file_path = tmp_path / "nested_data.pkl"
        test_data = {
            "users": [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
            ],
            "counts": [1, 2, 3],
            "active": True,
        }

        # Create a pickle file
        with file_path.open("wb") as f:
            pickle.dump(test_data, f)

        # Load the file
        result = pickle_load(file_path)

        # Verify the loaded data
        assert result == test_data

    def test_load_none_value(self, tmp_path: Path) -> None:
        """Test loading None value from a pickle file."""
        file_path = tmp_path / "none_data.pkl"
        test_data = None

        # Create a pickle file
        with file_path.open("wb") as f:
            pickle.dump(test_data, f)

        # Load the file
        result = pickle_load(file_path)

        # Verify the loaded data
        assert result is None

    def test_load_boolean_values(self, tmp_path: Path) -> None:
        """Test loading boolean values from a pickle file."""
        file_path = tmp_path / "bool_data.pkl"
        test_data = {"true": True, "false": False}

        # Create a pickle file
        with file_path.open("wb") as f:
            pickle.dump(test_data, f)

        # Load the file
        result = pickle_load(file_path)

        # Verify the loaded data
        assert result == test_data

    def test_load_numeric_types(self, tmp_path: Path) -> None:
        """Test loading various numeric types."""
        file_path = tmp_path / "numeric_data.pkl"
        test_data = {
            "integer": 42,
            "float": 3.14,
            "negative": -10,
            "zero": 0,
        }

        # Create a pickle file
        with file_path.open("wb") as f:
            pickle.dump(test_data, f)

        # Load the file
        result = pickle_load(file_path)

        # Verify the loaded data
        assert result == test_data

    def test_load_tuple_and_set(self, tmp_path: Path) -> None:
        """Test loading tuples and sets."""
        file_path = tmp_path / "collection_data.pkl"
        test_data = {"tuple": (1, 2, 3), "set": {4, 5, 6}}

        # Create a pickle file
        with file_path.open("wb") as f:
            pickle.dump(test_data, f)

        # Load the file
        result = pickle_load(file_path)

        # Verify the loaded data
        assert result == test_data

    def test_load_from_path_object(self, tmp_path: Path) -> None:
        """Test loading from a Path object instead of string."""
        file_path = tmp_path / "path_obj.pkl"
        test_data = {"test": "data"}

        # Create a pickle file
        with file_path.open("wb") as f:
            pickle.dump(test_data, f)

        # Load using Path object directly
        result = pickle_load(file_path)

        # Verify the loaded data
        assert result == test_data

    def test_load_large_data(self, tmp_path: Path) -> None:
        """Test loading large data structures."""
        file_path = tmp_path / "large_data.pkl"
        test_data = {
            "items": list(range(10000)),
            "nested": {i: i**2 for i in range(100)},
        }

        # Create a pickle file
        with file_path.open("wb") as f:
            pickle.dump(test_data, f)

        # Load the file
        result = pickle_load(file_path)

        # Verify the loaded data
        assert result == test_data
        assert len(result["items"]) == 10000

    def test_load_file_not_found_error(self, tmp_path: Path) -> None:
        """Test that FileNotFoundError is raised for non-existent file."""
        file_path = tmp_path / "nonexistent.pkl"

        # Attempt to load non-existent file
        with pytest.raises(FileNotFoundError):
            pickle_load(file_path)

    def test_load_empty_dict(self, tmp_path: Path) -> None:
        """Test loading an empty dictionary."""
        file_path = tmp_path / "empty_dict.pkl"
        test_data = {}

        # Create a pickle file
        with file_path.open("wb") as f:
            pickle.dump(test_data, f)

        # Load the file
        result = pickle_load(file_path)

        # Verify the loaded data
        assert result == {}

    def test_load_empty_list(self, tmp_path: Path) -> None:
        """Test loading an empty list."""
        file_path = tmp_path / "empty_list.pkl"
        test_data = []

        # Create a pickle file
        with file_path.open("wb") as f:
            pickle.dump(test_data, f)

        # Load the file
        result = pickle_load(file_path)

        # Verify the loaded data
        assert result == []

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
    def test_load_various_types(self, tmp_path: Path, test_data) -> None:
        """Test loading various data types."""
        file_path = tmp_path / "various_types.pkl"

        # Create a pickle file
        with file_path.open("wb") as f:
            pickle.dump(test_data, f)

        # Load the file
        result = pickle_load(file_path)

        # Verify the loaded data
        assert result == test_data
