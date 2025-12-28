# =============================================================================
# Test: nested_set
# =============================================================================

"""
Tests for rite.collections.tree.nested_set.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.collections.tree.nested_set import (
    NestedSetStructure,
)

# =============================================================================
# Test Class: NestedSetStructure
# =============================================================================


class TestNestedSetStructure:
    """Tests for NestedSetStructure class."""

    def test_instantiation(self) -> None:
        """Test NestedSetStructure can be instantiated."""
        instance = NestedSetStructure()
        assert len(instance) == 0

    def test_add(self) -> None:
        """Test NestedSetStructure.add() method."""
        instance = NestedSetStructure()
        instance.add("root")
        instance.add("child1", parent="root")
        instance.add("child2", parent="root")

        assert "root" in instance
        assert len(instance) == 3
        assert instance.children("root") == ["child1", "child2"]

    def test_children(self) -> None:
        """Test NestedSetStructure.children() method."""
        instance = NestedSetStructure()
        instance.add("root")
        instance.add("child", parent="root")

        assert instance.children("root") == ["child"]
        assert instance.children("child") == []
        assert instance.children("missing") == []

    def test_parent(self) -> None:
        """Test NestedSetStructure.parent() method."""
        instance = NestedSetStructure()
        instance.add("root")
        instance.add("child", parent="root")

        assert instance.parent("child") == "root"
        assert instance.parent("root") is None
        assert instance.parent("missing") is None

    def test_original(self) -> None:
        """Test NestedSetStructure.original() method."""
        instance = NestedSetStructure()

        a1 = ("a",)
        instance.add(a1)

        # Equal value should map back to stored canonical instance
        a2 = ("a",)
        assert instance.original(a2) is a1

        # Non-matching item should be returned as-is
        b = ("b",)
        assert instance.original(b) is b

    def test_nested_items(self) -> None:
        """Test NestedSetStructure.nested_items() method."""
        instance = NestedSetStructure()
        instance.add("root1")
        instance.add("child1", parent="root1")
        instance.add("child2", parent="root1")
        instance.add("root2")
        instance.add("child3", parent="root2")

        items = instance.nested_items()
        # Expect depth-first traversal respecting insertion order
        assert items == ["root1", "child1", "child2", "root2", "child3"]
    def test_add_duplicate(self) -> None:
        """Test adding the same item twice (early return path)."""
        instance = NestedSetStructure()
        instance.add("root")
        initial_len = len(instance)
        instance.add("root")  # Try to add again
        assert len(instance) == initial_len  # No new items added

    def test_iter(self) -> None:
        """Test __iter__ method for iteration over items."""
        instance = NestedSetStructure()
        instance.add("a")
        instance.add("b")
        instance.add("c")

        items = list(instance)
        assert "a" in items
        assert "b" in items
        assert "c" in items