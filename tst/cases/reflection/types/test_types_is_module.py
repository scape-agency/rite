# =============================================================================
# Test: types_is_module
# =============================================================================

"""
Tests for rite.reflection.types.types_is_module.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.reflection.types.types_is_module import (
    types_is_module,
)

# =============================================================================
# Test Functions
# =============================================================================


class TestTypesIsModule:
    """Tests for types_is_module function."""

    def test_json_module_returns_true(self) -> None:
        """Test that json module returns True."""
        # Import | Standard Library
        import json

        assert types_is_module(json)

    def test_math_module_returns_true(self) -> None:
        """Test that math module returns True."""
        # Import | Standard Library
        import math

        assert types_is_module(math)

    def test_os_module_returns_true(self) -> None:
        """Test that os module returns True."""
        # Import | Standard Library
        import os

        assert types_is_module(os)

    def test_sys_module_returns_true(self) -> None:
        """Test that sys module returns True."""
        # Import | Standard Library
        import sys

        assert types_is_module(sys)

    def test_string_returns_false(self) -> None:
        """Test that string returns False."""
        assert not types_is_module("not a module")

    def test_number_returns_false(self) -> None:
        """Test that number returns False."""
        assert not types_is_module(42)
        assert not types_is_module(3.14)

    def test_class_returns_false(self) -> None:
        """Test that class returns False."""
        assert not types_is_module(str)
        assert not types_is_module(int)
        assert not types_is_module(list)

    def test_instance_returns_false(self) -> None:
        """Test that instance returns False."""
        assert not types_is_module("hello")
        assert not types_is_module([])
        assert not types_is_module({})

    def test_function_returns_false(self) -> None:
        """Test that function returns False."""

        def my_func():
            pass

        assert not types_is_module(my_func)

    def test_none_returns_false(self) -> None:
        """Test that None returns False."""
        assert not types_is_module(None)

    def test_collections_module_returns_true(self) -> None:
        """Test that collections module returns True."""
        # Import | Standard Library
        import collections

        assert types_is_module(collections)

    def test_datetime_module_returns_true(self) -> None:
        """Test that datetime module returns True."""
        # Import | Standard Library
        import datetime

        assert types_is_module(datetime)
