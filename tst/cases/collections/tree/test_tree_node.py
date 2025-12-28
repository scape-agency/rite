# =============================================================================
# Test: tree_node
# =============================================================================

"""
Tests for rite.collections.tree.tree_node.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.tree.tree_node import (
    TreeNode,
)

# =============================================================================
# Test Class: TreeNode
# =============================================================================


class TestTreeNode:
    """Tests for TreeNode class."""

    def test_instantiation(self) -> None:
        """Test TreeNode can be instantiated."""
        instance = TreeNode(value="root")
        assert instance is not None
        assert instance.value == "root"
        assert len(instance.children) == 0
        assert instance.parent is None

    def test_add_child(self) -> None:
        """Test TreeNode.add_child() method."""
        parent = TreeNode(value="parent")
        child = TreeNode(value="child")
        parent.add_child(child)
        assert len(parent.children) == 1
        assert child.parent == parent

    def test_remove_child(self) -> None:
        """Test TreeNode.remove_child() method."""
        parent = TreeNode(value="parent")
        child = TreeNode(value="child")
        parent.add_child(child)
        parent.remove_child(child)
        assert len(parent.children) == 0
        assert child.parent is None

    def test_is_leaf(self) -> None:
        """Test TreeNode.is_leaf() method."""
        leaf = TreeNode(value="leaf")
        assert leaf.is_leaf() is True

        parent = TreeNode(value="parent")
        child = TreeNode(value="child")
        parent.add_child(child)
        assert parent.is_leaf() is False

    def test_is_root(self) -> None:
        """Test TreeNode.is_root() method."""
        root = TreeNode(value="root")
        assert root.is_root() is True

        child = TreeNode(value="child")
        root.add_child(child)
        assert child.is_root() is False

    def test_get_depth(self) -> None:
        """Test TreeNode.get_depth() method."""
        root = TreeNode(value="root")
        child = TreeNode(value="child")
        grandchild = TreeNode(value="grandchild")
        root.add_child(child)
        child.add_child(grandchild)

        assert root.get_depth() == 0
        assert child.get_depth() == 1
        assert grandchild.get_depth() == 2

    def test_get_height(self) -> None:
        """Test TreeNode.get_height() method."""
        root = TreeNode(value="root")
        child = TreeNode(value="child")
        grandchild = TreeNode(value="grandchild")
        root.add_child(child)
        child.add_child(grandchild)

        assert grandchild.get_height() == 0
        assert child.get_height() == 1
        assert root.get_height() == 2

    def test_get_siblings(self) -> None:
        """Test TreeNode.get_siblings() method."""
        parent = TreeNode(value="parent")
        child1 = TreeNode(value="child1")
        child2 = TreeNode(value="child2")
        child3 = TreeNode(value="child3")
        parent.add_child(child1)
        parent.add_child(child2)
        parent.add_child(child3)

        siblings = child1.get_siblings()
        assert len(siblings) == 2
        assert child2 in siblings
        assert child3 in siblings

    def test_get_ancestors(self) -> None:
        """Test TreeNode.get_ancestors() method."""
        root = TreeNode(value="root")
        child = TreeNode(value="child")
        grandchild = TreeNode(value="grandchild")
        root.add_child(child)
        child.add_child(grandchild)

        ancestors = grandchild.get_ancestors()
        assert len(ancestors) == 2
        assert ancestors[0] == child
        assert ancestors[1] == root

    def test_traverse_preorder(self) -> None:
        """Test TreeNode.traverse_preorder() method."""
        root = TreeNode(value=1)
        child1 = TreeNode(value=2)
        child2 = TreeNode(value=3)
        root.add_child(child1)
        root.add_child(child2)

        result = list(root.traverse_preorder())
        values = [node.value for node in result]
        assert values == [1, 2, 3]

    def test_traverse_postorder(self) -> None:
        """Test TreeNode.traverse_postorder() method."""
        root = TreeNode(value=1)
        child1 = TreeNode(value=2)
        child2 = TreeNode(value=3)
        root.add_child(child1)
        root.add_child(child2)

        result = list(root.traverse_postorder())
        values = [node.value for node in result]
        assert values == [2, 3, 1]

    def test_traverse_levelorder(self) -> None:
        """Test TreeNode.traverse_levelorder() method."""
        root = TreeNode(value=1)
        child1 = TreeNode(value=2)
        child2 = TreeNode(value=3)
        grandchild = TreeNode(value=4)
        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild)

        result = list(root.traverse_levelorder())
        values = [node.value for node in result]
        assert values == [1, 2, 3, 4]
