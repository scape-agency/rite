# =============================================================================
# Test: binary_tree_node
# =============================================================================

"""
Tests for rite.collections.tree.binary_tree_node.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.tree.binary_tree_node import (
    BinaryTreeNode,
)

# =============================================================================
# Test Class: BinaryTreeNode
# =============================================================================


class TestBinaryTreeNode:
    """Tests for BinaryTreeNode class."""

    def test_instantiation(self) -> None:
        """Test BinaryTreeNode can be instantiated."""
        instance = BinaryTreeNode(value=10)
        assert instance is not None
        assert instance.value == 10
        assert instance.left is None
        assert instance.right is None

    def test_is_leaf(self) -> None:
        """Test BinaryTreeNode.is_leaf() method."""
        leaf = BinaryTreeNode(value=10)
        assert leaf.is_leaf() is True

        node = BinaryTreeNode(value=5, left=BinaryTreeNode(value=3))
        assert node.is_leaf() is False

    def test_has_left_child(self) -> None:
        """Test BinaryTreeNode.has_left_child() method."""
        node = BinaryTreeNode(value=10)
        assert node.has_left_child() is False

        node.left = BinaryTreeNode(value=5)
        assert node.has_left_child() is True

    def test_has_right_child(self) -> None:
        """Test BinaryTreeNode.has_right_child() method."""
        node = BinaryTreeNode(value=10)
        assert node.has_right_child() is False

        node.right = BinaryTreeNode(value=15)
        assert node.has_right_child() is True

    def test_get_height(self) -> None:
        """Test BinaryTreeNode.get_height() method."""
        leaf = BinaryTreeNode(value=10)
        assert leaf.get_height() == 0

        root = BinaryTreeNode(value=10, left=BinaryTreeNode(value=5))
        assert root.get_height() == 1

    def test_inorder_traversal(self) -> None:
        """Test BinaryTreeNode.inorder_traversal() method."""
        root = BinaryTreeNode(
            value=2,
            left=BinaryTreeNode(value=1),
            right=BinaryTreeNode(value=3),
        )
        result = root.inorder_traversal()
        values = [node.value for node in result]
        assert values == [1, 2, 3]

    def test_traverse_inorder(self) -> None:
        """Test BinaryTreeNode.traverse_inorder() method."""
        root = BinaryTreeNode(
            value=2,
            left=BinaryTreeNode(value=1),
            right=BinaryTreeNode(value=3),
        )
        result = list(root.traverse_inorder())
        values = [node.value for node in result]
        assert values == [1, 2, 3]

    def test_preorder_traversal(self) -> None:
        """Test BinaryTreeNode.preorder_traversal() method."""
        root = BinaryTreeNode(
            value=2,
            left=BinaryTreeNode(value=1),
            right=BinaryTreeNode(value=3),
        )
        result = root.preorder_traversal()
        values = [node.value for node in result]
        assert values == [2, 1, 3]

    def test_traverse_preorder(self) -> None:
        """Test BinaryTreeNode.traverse_preorder() method."""
        root = BinaryTreeNode(
            value=2,
            left=BinaryTreeNode(value=1),
            right=BinaryTreeNode(value=3),
        )
        result = list(root.traverse_preorder())
        values = [node.value for node in result]
        assert values == [2, 1, 3]

    def test_postorder_traversal(self) -> None:
        """Test BinaryTreeNode.postorder_traversal() method."""
        root = BinaryTreeNode(
            value=2,
            left=BinaryTreeNode(value=1),
            right=BinaryTreeNode(value=3),
        )
        result = root.postorder_traversal()
        values = [node.value for node in result]
        assert values == [1, 3, 2]

    def test_traverse_postorder(self) -> None:
        """Test BinaryTreeNode.traverse_postorder() method."""
        root = BinaryTreeNode(
            value=2,
            left=BinaryTreeNode(value=1),
            right=BinaryTreeNode(value=3),
        )
        result = list(root.traverse_postorder())
        values = [node.value for node in result]
        assert values == [1, 3, 2]
