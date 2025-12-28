# =============================================================================
# Test: types_is_function
# =============================================================================

"""
Tests for rite.reflection.types.types_is_function.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.reflection.types.types_is_function import (
    types_is_function,
)

# =============================================================================
# Test Functions
# =============================================================================


class TestTypesIsFunction:
    """Tests for types_is_function function."""

    def test_function_returns_true(self) -> None:
        """Test that function returns True."""

        def my_func():
            pass

        assert types_is_function(my_func)

    def test_lambda_returns_true(self) -> None:
        """Test that lambda returns True."""
        assert types_is_function(lambda x: x)
        assert types_is_function(lambda x, y: x + y)

    def test_builtin_function_returns_false(self) -> None:
        """Test that builtin functions return False."""
        # len, print, etc. are not caught by isfunction
        # They are builtin_function_or_method
        assert not types_is_function(len)
        assert not types_is_function(print)

    def test_class_returns_false(self) -> None:
        """Test that class returns False."""
        assert not types_is_function(str)
        assert not types_is_function(int)
        assert not types_is_function(list)

    def test_instance_returns_false(self) -> None:
        """Test that instance returns False."""
        assert not types_is_function("hello")
        assert not types_is_function(42)
        assert not types_is_function([])

    def test_method_returns_false(self) -> None:
        """Test that method returns False."""
        # Methods are not functions (they're bound methods)
        assert not types_is_function("hello".upper)
        assert not types_is_function([].append)

    def test_unbound_method_returns_true(self) -> None:
        """Test that unbound method function returns True."""

        class MyClass:
            def method(self):
                pass

        # Accessing from class (not instance) gives a function
        assert types_is_function(MyClass.method)

    def test_module_returns_false(self) -> None:
        """Test that module returns False."""
        # Import | Standard Library
        import json

        assert not types_is_function(json)

    def test_nested_function_returns_true(self) -> None:
        """Test that nested function returns True."""

        def outer():
            def inner():
                pass

            return inner

        inner_func = outer()
        assert types_is_function(inner_func)

    def test_staticmethod_returns_true(self) -> None:
        """Test with static method."""

        class MyClass:
            @staticmethod
            def static_func():
                pass

        # When accessed via the class, static methods are functions
        assert types_is_function(MyClass.static_func)
