# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
JSON Utilities Module
====================

Provides utilities for JSON data operations using only Python's standard library.

This module offers a JSONHandler class with methods for:
- Reading and writing JSON files
- Validating JSON data
- Merging, filtering, and transforming JSON structures
- Pretty printing and formatting
- Path-based extraction and updates

All functionality uses only Python stdlib (json, csv modules).

Example:
    >>> from rite.serialization import JSONHandler
    >>> handler = JSONHandler()
    >>> data = handler.read_json("config.json")
    >>> handler.write_json("output.json", data, indent=2)

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import csv
import json
from typing import Any, Callable, Dict, List

# =============================================================================
# Classes
# =============================================================================


class JSONHandler:
    """
    A class for handling JSON data operations using stdlib only.

    Methods
    -------
    read_json(file_path: str) -> Any:
        Reads JSON data from a file and returns it.
    write_json(file_path: str, data: Any, indent: int = 4):
        Writes JSON data to a file.
    validate_json(data: str) -> bool:
        Validates a JSON string.
    pretty_print_json(data: Any):
        Prints JSON data in a formatted manner.
    merge_json(json1: Dict, json2: Dict) -> Dict:
        Merges two JSON objects.
    find_in_json(data: Dict, key: str) -> Any:
        Finds a value by key in nested JSON.
    filter_json(data: Dict, filter_func: Callable[[Dict], bool]) -> Dict:
        Filters JSON data based on a function.
    update_json(data: Dict, updates: Dict) -> Dict:
        Updates JSON data with new values.
    flatten_json(data: Dict, parent_key: str = "", sep: str = ".") -> Dict:
        Flattens nested JSON structure.
    deep_merge_json(json1: Dict, json2: Dict) -> Dict:
        Performs a deep merge of two JSON objects.
    sort_json(data: Dict, by_key=True, reverse=False) -> Dict:
        Sorts JSON data.
    diff_json(json1: Dict, json2: Dict) -> Dict:
        Computes the difference between two JSON objects.
    extract_keys(data: Dict) -> List[str]:
        Extracts all keys from nested JSON.
    json_to_csv(json_data: list[dict], csv_file: str):
        Converts JSON array to CSV file.
    csv_to_json(csv_file: str) -> List[Dict]:
        Converts CSV file to JSON array.
    """

    @staticmethod
    def read_json(file_path: str) -> Any:
        """
        Reads JSON data from a file.

        Parameters
        ----------
        file_path : str
            The path to the JSON file.

        Returns
        -------
        Any
            The data read from the JSON file.

        Raises
        ------
        Exception
            If file cannot be read or parsed.
        """
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def write_json(file_path: str, data: Any, indent: int = 4) -> None:
        """
        Writes JSON data to a file.

        Parameters
        ----------
        file_path : str
            The path to the JSON file.
        data : Any
            The data to write.
        indent : int, optional
            Number of spaces for indentation (default: 4).
        """
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=indent, ensure_ascii=False)

    @staticmethod
    def validate_json(data: str) -> bool:
        """
        Validates a JSON string.

        Parameters
        ----------
        data : str
            The JSON string to validate.

        Returns
        -------
        bool
            True if valid JSON, False otherwise.
        """
        try:
            json.loads(data)
            return True
        except (json.JSONDecodeError, TypeError):
            return False

    @staticmethod
    def pretty_print_json(data: Any) -> None:
        """
        Prints JSON data in a formatted manner.

        Parameters
        ----------
        data : Any
            The data to print.
        """
        print(json.dumps(data, indent=4, ensure_ascii=False))

    @staticmethod
    def merge_json(json1: Dict, json2: Dict) -> Dict:
        """
        Merges two JSON objects (shallow merge).

        Parameters
        ----------
        json1 : Dict
            First JSON object.
        json2 : Dict
            Second JSON object (takes precedence).

        Returns
        -------
        Dict
            Merged JSON object.
        """
        return {**json1, **json2}

    @staticmethod
    def find_in_json(data: Dict, key: str) -> Any:
        """
        Finds a value by key in nested JSON structure.

        Parameters
        ----------
        data : Dict
            The JSON data to search.
        key : str
            The key to find.

        Returns
        -------
        Any
            The value if found, None otherwise.
        """
        if key in data:
            return data[key]
        for value in data.values():
            if isinstance(value, dict):
                result = JSONHandler.find_in_json(value, key)
                if result is not None:
                    return result
        return None

    @staticmethod
    def filter_json(data: Dict, filter_func: Callable[[Any], bool]) -> Dict:
        """
        Filters JSON data based on a filter function.

        Parameters
        ----------
        data : Dict
            The JSON data to filter.
        filter_func : Callable[[Any], bool]
            Function that returns True for items to keep.

        Returns
        -------
        Dict
            Filtered JSON data.
        """
        return {k: v for k, v in data.items() if filter_func(v)}

    @staticmethod
    def update_json(data: Dict, updates: Dict) -> Dict:
        """
        Updates JSON data with new values.

        Parameters
        ----------
        data : Dict
            Original JSON data.
        updates : Dict
            Updates to apply.

        Returns
        -------
        Dict
            Updated JSON data.
        """
        data.update(updates)
        return data

    @staticmethod
    def flatten_json(data: Dict, parent_key: str = "", sep: str = ".") -> Dict:
        """
        Flattens a nested JSON structure.

        Parameters
        ----------
        data : Dict
            Nested JSON data.
        parent_key : str, optional
            Parent key for recursion (default: "").
        sep : str, optional
            Separator for flattened keys (default: ".").

        Returns
        -------
        Dict
            Flattened JSON data.
        """
        items: list[tuple] = []
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(
                    JSONHandler.flatten_json(v, new_key, sep=sep).items()
                )
            else:
                items.append((new_key, v))
        return dict(items)

    @staticmethod
    def deep_merge_json(json1: Dict, json2: Dict) -> Dict:
        """
        Performs a deep merge of two JSON objects.

        Parameters
        ----------
        json1 : Dict
            First JSON object.
        json2 : Dict
            Second JSON object (takes precedence).

        Returns
        -------
        Dict
            Deep merged JSON object.
        """
        result = json1.copy()
        for key, value in json2.items():
            if (
                key in result
                and isinstance(result[key], dict)
                and isinstance(value, dict)
            ):
                result[key] = JSONHandler.deep_merge_json(result[key], value)
            else:
                result[key] = value
        return result

    @staticmethod
    def sort_json(
        data: Dict, by_key: bool = True, reverse: bool = False
    ) -> Dict:
        """
        Sorts JSON data by keys or values.

        Parameters
        ----------
        data : Dict
            JSON data to sort.
        by_key : bool, optional
            If True, sort by keys; if False, sort by values (default: True).
        reverse : bool, optional
            If True, sort in descending order (default: False).

        Returns
        -------
        Dict
            Sorted JSON data.
        """
        if by_key:
            return dict(
                sorted(data.items(), key=lambda x: x[0], reverse=reverse)
            )
        else:
            return dict(
                sorted(data.items(), key=lambda x: x[1], reverse=reverse)
            )

    @staticmethod
    def diff_json(json1: Dict, json2: Dict) -> Dict:
        """
        Computes the difference between two JSON objects.

        Parameters
        ----------
        json1 : Dict
            First JSON object.
        json2 : Dict
            Second JSON object.

        Returns
        -------
        Dict
            Dictionary showing differences with keys: 'added', 'removed', 'modified'.
        """
        added = {k: v for k, v in json2.items() if k not in json1}
        removed = {k: v for k, v in json1.items() if k not in json2}
        modified = {
            k: {"old": json1[k], "new": json2[k]}
            for k in json1
            if k in json2 and json1[k] != json2[k]
        }
        return {"added": added, "removed": removed, "modified": modified}

    @staticmethod
    def extract_keys(data: Dict) -> List[str]:
        """
        Extracts all keys from nested JSON structure.

        Parameters
        ----------
        data : Dict
            JSON data.

        Returns
        -------
        List[str]
            List of all keys.
        """
        keys = list(data.keys())
        for value in data.values():
            if isinstance(value, dict):
                keys.extend(JSONHandler.extract_keys(value))
        return keys

    @staticmethod
    def json_to_csv(json_data: list[dict], csv_file: str) -> None:
        """
        Converts JSON array to CSV file.

        Parameters
        ----------
        json_data : List[Dict]
            List of JSON objects.
        csv_file : str
            Output CSV file path.
        """
        if not json_data:
            return

        keys = json_data[0].keys()
        with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(json_data)

    @staticmethod
    def csv_to_json(csv_file: str) -> List[Dict]:
        """
        Converts CSV file to JSON array.

        Parameters
        ----------
        csv_file : str
            Input CSV file path.

        Returns
        -------
        List[Dict]
            List of JSON objects.
        """
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            return list(reader)


# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "JSONHandler",
]
