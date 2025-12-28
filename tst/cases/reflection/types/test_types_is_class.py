# =============================================================================
# Test: types_is_class
# =============================================================================

"""
Tests for rite.reflection.types.types_is_class.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.reflection.types.types_is_class import (
    types_is_class,
)

# =============================================================================
# Test Functions
# =============================================================================


class TestTypesIsClass:
    """Tests for types_is_class function."""

    def test_class_returns_true(self) -> None:
        """Test that class returns True."""
        assert types_is_class(str)
        assert types_is_class(int)
        assert types_is_class(list)
        assert types_is_class(dict)

    def test_instance_returns_false(self) -> None:
        """Test that instance returns False."""
        assert not types_is_class("hello")
        assert not types_is_class(42)
        assert not types_is_class([])
        assert not types_is_class({})

    def test_custom_class_returns_true(self) -> None:
        """Test that custom class returns True."""
        class MyClass:
            pass
        
        assert types_is_class(MyClass)

    def test_custom_instance_returns_false(self) -> None:
        """Test that custom instance returns False."""
        class MyClass:
            pass
        
        obj = MyClass()
        assert not types_is_class(obj)

    def test_function_returns_false(self) -> None:
        """Test that function returns False."""
        def my_func():
            pass
        
        assert not types_is_class(my_func)

    def test_lambda_returns_false(self) -> None:
        """Test that lambda returns False."""
        assert not types_is_class(lambda x: x)

    def test_builtin_types_return_true(self) -> None:
        """Test that builtin types return True."""
        assert types_is_class(bool)
        assert types_is_class(float)
        assert types_is_class(tuple)
        assert types_is_class(set)

    def test_module_returns_false(self) -> None:
        """Test that module returns False."""
        import json
        assert not types_is_class(json)

    def test_none_returns_false(self) -> None:
        """Test that None returns False."""
        assert not types_is_class(None)

    def test_type_returns_true(self) -> None:
        """Test that type itself returns True."""
        assert types_is_class(type)
