# =============================================================================
# Test: types_to_list
# =============================================================================

"""
Tests for rite.conversion.types.types_to_list.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.types.types_to_list import (
    types_to_list,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_types_to_list_basic_iterables() -> None:
    """Test conversion of common iterables to list."""
    values = [1, 2, 3]
    assert types_to_list(values) is values

    assert types_to_list((1, 2, 3)) == [1, 2, 3]

    result = types_to_list({1, 2, 3})
    assert sorted(result) == [1, 2, 3]


def test_types_to_list_strings_and_scalars() -> None:
    """Test string handling and non-iterable scalars."""
    assert types_to_list("hello", split_strings=True) == [
        "h",
        "e",
        "l",
        "l",
        "o",
    ]
    assert types_to_list("hello", split_strings=False) == ["hello"]
    assert types_to_list(42) == [42]
    assert types_to_list(None) == [None]
