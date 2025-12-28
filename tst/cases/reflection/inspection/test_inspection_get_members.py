# =============================================================================
# Test: inspection_get_members
# =============================================================================

"""
Tests for rite.reflection.inspection.inspection_get_members.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import inspect

# Import | Libraries
import pytest

# Import | Local Modules
from rite.reflection.inspection.inspection_get_members import (
    inspection_get_members,
)

# =============================================================================
# Test Functions
# =============================================================================


class TestInspectionGetMembers:
    """Tests for inspection_get_members function."""

    def test_returns_list_of_tuples(self) -> None:
        """Test that function returns list of tuples."""
        import json
        result = inspection_get_members(json)
        assert isinstance(result, list)
        assert all(isinstance(item, tuple) and len(item) == 2 for item in result)

    def test_contains_members(self) -> None:
        """Test that result contains members."""
        import json
        result = inspection_get_members(json)
        names = [name for name, _ in result]
        assert len(names) > 0
        # json has dumps function
        assert "dumps" in names

    def test_with_predicate_filter(self) -> None:
        """Test with predicate filter."""
        import json
        result = inspection_get_members(json, inspect.isfunction)
        assert isinstance(result, list)
        # All items should be functions when using isfunction predicate
        if result:
            for name, member in result:
                assert inspect.isfunction(member)

    def test_with_isclass_predicate(self) -> None:
        """Test with isclass predicate."""
        import collections
        result = inspection_get_members(collections, inspect.isclass)
        assert isinstance(result, list)
        # collections module has classes
        assert len(result) > 0
        # All items should be classes
        for name, member in result:
            assert inspect.isclass(member)

    def test_none_predicate(self) -> None:
        """Test with None predicate."""
        class SimpleClass:
            x = 10
            def method(self):
                pass
        
        result = inspection_get_members(SimpleClass, None)
        assert isinstance(result, list)
        assert len(result) > 0

    def test_tuple_structure(self) -> None:
        """Test that each tuple has name and member."""
        import json
        result = inspection_get_members(json)
        if result:
            for name, member in result:
                assert isinstance(name, str)

    def test_all_members_returned(self) -> None:
        """Test that all members are in result."""
        class TestClass:
            attr1 = 10
            attr2 = "hello"
            
            def method1(self):
                pass
        
        result = inspection_get_members(TestClass)
        names = [name for name, _ in result]
        # __init__, __doc__, etc. will be present
        assert len(names) > 0
