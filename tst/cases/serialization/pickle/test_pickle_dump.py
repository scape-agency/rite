# =============================================================================
# Test: pickle_dump
# =============================================================================

"""
Tests for rite.serialization.pickle.pickle_dump.
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
from rite.serialization.pickle.pickle_dump import (
    pickle_dump,
)

# =============================================================================
# Test Classes
# =============================================================================


class TestPickleDump:
    """Tests for pickle_dump() function."""

    def test_dump_dict_to_file(self, tmp_path: Path) -> None:
        """Test dumping a dictionary to a pickle file."""
        file_path = tmp_path / "data.pkl"
        test_data = {"key": "value", "number": 42}

        pickle_dump(str(file_path), test_data)

        # Verify the file was created
        assert file_path.exists()

        # Verify the contents by loading the file
        with file_path.open("rb") as f:
            loaded_data = pickle.load(f)

        assert loaded_data == test_data

    def test_dump_list_to_file(self, tmp_path: Path) -> None:
        """Test dumping a list to a pickle file."""
        file_path = tmp_path / "list_data.pkl"
        test_data = [1, 2, 3, 4, 5]

        pickle_dump(file_path, test_data)

        # Verify the file was created and contains correct data
        with file_path.open("rb") as f:
            loaded_data = pickle.load(f)

        assert loaded_data == test_data

    def test_dump_string_to_file(self, tmp_path: Path) -> None:
        """Test dumping a string to a pickle file."""
        file_path = tmp_path / "string_data.pkl"
        test_data = "Hello, World!"

        pickle_dump(file_path, test_data)

        # Verify the file was created and contains correct data
        with file_path.open("rb") as f:
            loaded_data = pickle.load(f)

        assert loaded_data == test_data

    def test_dump_nested_structure(self, tmp_path: Path) -> None:
        """Test dumping complex nested data structures."""
        file_path = tmp_path / "nested_data.pkl"
        test_data = {
            "users": [
                {"name": "Alice", "age": 30},
                {"name": "Bob", "age": 25},
            ],
            "counts": [1, 2, 3],
            "active": True,
        }

        pickle_dump(file_path, test_data)

        # Verify the file was created and contains correct data
        with file_path.open("rb") as f:
            loaded_data = pickle.load(f)

        assert loaded_data == test_data

    def test_dump_none_value(self, tmp_path: Path) -> None:
        """Test dumping None value to a pickle file."""
        file_path = tmp_path / "none_data.pkl"
        test_data = None

        pickle_dump(file_path, test_data)

        # Verify the file was created and contains None
        with file_path.open("rb") as f:
            loaded_data = pickle.load(f)

        assert loaded_data is None

    def test_dump_boolean_values(self, tmp_path: Path) -> None:
        """Test dumping boolean values to a pickle file."""
        file_path = tmp_path / "bool_data.pkl"
        test_data = {"true": True, "false": False}

        pickle_dump(file_path, test_data)

        # Verify the file was created and contains correct data
        with file_path.open("rb") as f:
            loaded_data = pickle.load(f)

        assert loaded_data == test_data

    def test_dump_numeric_types(self, tmp_path: Path) -> None:
        """Test dumping various numeric types."""
        file_path = tmp_path / "numeric_data.pkl"
        test_data = {
            "integer": 42,
            "float": 3.14,
            "negative": -10,
            "zero": 0,
        }

        pickle_dump(file_path, test_data)

        # Verify the file was created and contains correct data
        with file_path.open("rb") as f:
            loaded_data = pickle.load(f)

        assert loaded_data == test_data

    def test_dump_tuple_and_set(self, tmp_path: Path) -> None:
        """Test dumping tuples and sets."""
        file_path = tmp_path / "collection_data.pkl"
        test_data = {"tuple": (1, 2, 3), "set": {4, 5, 6}}

        pickle_dump(file_path, test_data)

        # Verify the file was created and contains correct data
        with file_path.open("rb") as f:
            loaded_data = pickle.load(f)

        assert loaded_data == test_data

    def test_dump_creates_parent_directories(self, tmp_path: Path) -> None:
        """Test that parent directories are created if they don't exist."""
        file_path = tmp_path / "subdir1" / "subdir2" / "data.pkl"
        test_data = {"key": "value"}

        pickle_dump(file_path, test_data)

        # Verify the file and parent directories were created
        assert file_path.exists()
        assert file_path.parent.exists()

        # Verify the contents
        with file_path.open("rb") as f:
            loaded_data = pickle.load(f)

        assert loaded_data == test_data

    def test_dump_overwrites_existing_file(self, tmp_path: Path) -> None:
        """Test that dumping overwrites an existing file."""
        file_path = tmp_path / "overwrite.pkl"

        # Create initial file
        initial_data = {"old": "data"}
        pickle_dump(file_path, initial_data)

        # Overwrite with new data
        new_data = {"new": "content"}
        pickle_dump(file_path, new_data)

        # Verify the file contains the new data
        with file_path.open("rb") as f:
            loaded_data = pickle.load(f)

        assert loaded_data == new_data

    def test_dump_with_path_object(self, tmp_path: Path) -> None:
        """Test dumping with a Path object instead of string."""
        file_path = tmp_path / "path_obj.pkl"
        test_data = {"test": "data"}

        # Use Path object directly
        pickle_dump(file_path, test_data)

        # Verify the file was created and contains correct data
        with file_path.open("rb") as f:
            loaded_data = pickle.load(f)

        assert loaded_data == test_data

    @pytest.mark.parametrize(
        "test_data",
        [
            {"single": "item"},
            [42],
            "text",
            123,
            3.14,
            True,
            None,
            [],
            {},
        ],
    )
    def test_dump_various_types(self, tmp_path: Path, test_data) -> None:
        """Test dumping various data types."""
        file_path = tmp_path / "various_types.pkl"

        pickle_dump(file_path, test_data)

        # Verify the file was created and contains correct data
        with file_path.open("rb") as f:
            loaded_data = pickle.load(f)

        assert loaded_data == test_data
