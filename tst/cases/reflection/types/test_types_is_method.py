# =============================================================================
# Test: types_is_method
# =============================================================================

"""
Tests for rite.reflection.types.types_is_method.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.reflection.types.types_is_method import (
    types_is_method,
)

# =============================================================================
# Test Functions
# =============================================================================


class TestTypesIsMethod:
    """Tests for types_is_method function."""

    def test_string_method_returns_true(self) -> None:
        """Test that custom class method returns True."""

        # Built-in methods are not caught by inspect.ismethod, so test with custom class
        class MyClass:
            def my_method(self):
                pass

        obj = MyClass()
        assert types_is_method(obj.my_method)

    def test_list_method_returns_true(self) -> None:
        """Test that custom instance method returns True."""

        class ListWrapper:
            def append(self, item):
                pass

        obj = ListWrapper()
        assert types_is_method(obj.append)

    def test_dict_method_returns_true(self) -> None:
        """Test that custom instance method returns True."""

        class DictWrapper:
            def get(self, key):
                pass

            def keys(self):
                pass

        obj = DictWrapper()
        assert types_is_method(obj.get)
        assert types_is_method(obj.keys)

    def test_custom_instance_method_returns_true(self) -> None:
        """Test that custom instance method returns True."""

        class MyClass:
            def method(self):
                pass

        obj = MyClass()
        assert types_is_method(obj.method)

    def test_unbound_method_returns_false(self) -> None:
        """Test that unbound method returns False."""

        class MyClass:
            def method(self):
                pass

        # Accessing from class gives a function, not a method
        assert not types_is_method(MyClass.method)

    def test_function_returns_false(self) -> None:
        """Test that function returns False."""

        def my_func():
            pass

        assert not types_is_method(my_func)

    def test_lambda_returns_false(self) -> None:
        """Test that lambda returns False."""
        assert not types_is_method(lambda x: x)

    def test_class_returns_false(self) -> None:
        """Test that class returns False."""
        assert not types_is_method(str)
        assert not types_is_method(int)

    def test_instance_returns_false(self) -> None:
        """Test that instance returns False."""
        assert not types_is_method("hello")
        assert not types_is_method(42)

    def test_module_returns_false(self) -> None:
        """Test that module returns False."""
        # Import | Standard Library
        import json

        assert not types_is_method(json)

    def test_staticmethod_returns_false(self) -> None:
        """Test that staticmethod returns False."""

        class MyClass:
            @staticmethod
            def static_func():
                pass

        obj = MyClass()
        # Static methods are not bound methods
        assert not types_is_method(obj.static_func)
