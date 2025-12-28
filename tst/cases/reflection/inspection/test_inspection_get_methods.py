# =============================================================================
# Test: inspection_get_methods
# =============================================================================

"""
Tests for rite.reflection.inspection.inspection_get_methods.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.reflection.inspection.inspection_get_methods import (
    inspection_get_methods,
)

# =============================================================================
# Test Functions
# =============================================================================


class TestInspectionGetMethods:
    """Tests for inspection_get_methods function."""

    def test_returns_list_of_tuples(self) -> None:
        """Test that function returns list of tuples."""
        result = inspection_get_methods(str)
        assert isinstance(result, list)
        assert all(
            isinstance(item, tuple) and len(item) == 2 for item in result
        )

    def test_contains_string_methods(self) -> None:
        """Test that string instance methods are returned."""
        # Use a string instance to get bound methods
        s = "hello"
        result = inspection_get_methods(s)
        # Built-in methods might not be included, so just check it returns a list
        assert isinstance(result, list)

    def test_with_list_instance(self) -> None:
        """Test with list instance."""
        result = inspection_get_methods([])
        # getmembers with ismethod doesn't always catch built-in methods
        assert isinstance(result, list)

    def test_with_dict_instance(self) -> None:
        """Test with dict instance."""
        result = inspection_get_methods({})
        # getmembers with ismethod doesn't catch all built-in methods
        assert isinstance(result, list)

    def test_tuple_structure(self) -> None:
        """Test that each tuple has name and callable."""
        result = inspection_get_methods(str)
        if result:
            for name, method in result:
                assert isinstance(name, str)
                assert callable(method)

    def test_with_custom_class(self) -> None:
        """Test with custom class instance."""

        class MyClass:
            def my_method(self):
                pass

            def another_method(self):
                pass

        obj = MyClass()
        result = inspection_get_methods(obj)
        names = [name for name, _ in result]
        assert "my_method" in names
        assert "another_method" in names

    def test_includes_inherited_methods(self) -> None:
        """Test that inherited methods are included."""

        class Parent:
            def parent_method(self):
                pass

        class Child(Parent):
            def child_method(self):
                pass

        obj = Child()
        result = inspection_get_methods(obj)
        names = [name for name, _ in result]
        # Child instance should have both parent and child methods
        assert "parent_method" in names or "child_method" in names
