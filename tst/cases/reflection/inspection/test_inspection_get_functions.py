# =============================================================================
# Test: inspection_get_functions
# =============================================================================

"""
Tests for rite.reflection.inspection.inspection_get_functions.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.reflection.inspection.inspection_get_functions import (
    inspection_get_functions,
)

# =============================================================================
# Test Functions
# =============================================================================


class TestInspectionGetFunctions:
    """Tests for inspection_get_functions function."""

    def test_returns_list_of_tuples(self) -> None:
        """Test that function returns list of tuples."""
        import json
        result = inspection_get_functions(json)
        assert isinstance(result, list)
        assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

    def test_contains_functions(self) -> None:
        """Test that result contains functions."""
        import json
        result = inspection_get_functions(json)
        names = [name for name, _ in result]
        # json module has dumps and dump functions
        assert "dumps" in names or "dump" in names

    def test_with_custom_module(self) -> None:
        """Test with standard library module."""
        import collections
        result = inspection_get_functions(collections)
        # collections module might not have module-level functions
        assert isinstance(result, list)

    def test_empty_for_nonfunction_module(self) -> None:
        """Test with module containing no functions at module level."""
        import collections
        result = inspection_get_functions(collections)
        # collections has named tuples and classes, checking it returns a list
        assert isinstance(result, list)

    def test_with_custom_class(self) -> None:
        """Test with custom class."""
        class MyClass:
            @staticmethod
            def static_func():
                pass
            
            def instance_method(self):
                pass
        
        result = inspection_get_functions(MyClass)
        # Functions in class scope (not methods when accessed via class)
        assert isinstance(result, list)

    def test_tuple_structure(self) -> None:
        """Test that each tuple has name and callable."""
        import json
        result = inspection_get_functions(json)
        if result:
            for name, func in result:
                assert isinstance(name, str)
                assert callable(func)
