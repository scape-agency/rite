# -*- coding: utf-8 -*-

"""Tests for BinaryTreeNode."""

# Import | Local Modules
from src.rite.collections.tree import BinaryTreeNode


class TestBinaryTreeNode:
    """Test cases for BinaryTreeNode class."""

    def test_init(self):
        """Test node initialization."""
        node = BinaryTreeNode(1)
        assert node.value == 1
        assert node.left is None
        assert node.right is None

    def test_init_with_children(self):
        """Test initialization with children."""
        left = BinaryTreeNode(2)
        right = BinaryTreeNode(3)
        node = BinaryTreeNode(1, left=left, right=right)

        assert node.left is left
        assert node.right is right

    def test_is_leaf(self):
        """Test leaf detection."""
        leaf = BinaryTreeNode(1)
        assert leaf.is_leaf()

        parent = BinaryTreeNode(2)
        parent.left = leaf
        assert not parent.is_leaf()

    def test_has_left_child(self):
        """Test left child detection."""
        node = BinaryTreeNode(1)
        assert not node.has_left_child()

        node.left = BinaryTreeNode(2)
        assert node.has_left_child()

    def test_has_right_child(self):
        """Test right child detection."""
        node = BinaryTreeNode(1)
        assert not node.has_right_child()

        node.right = BinaryTreeNode(2)
        assert node.has_right_child()

    def test_get_height(self):
        """Test height calculation."""
        root = BinaryTreeNode(1)
        assert root.get_height() == 0

        root.left = BinaryTreeNode(2)
        assert root.get_height() == 1

        root.right = BinaryTreeNode(3)
        root.left.left = BinaryTreeNode(4)
        assert root.get_height() == 2

    def test_traverse_inorder(self):
        """Test in-order traversal."""
        root = BinaryTreeNode(4)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(6)
        root.left.left = BinaryTreeNode(1)
        root.left.right = BinaryTreeNode(3)
        root.right.left = BinaryTreeNode(5)
        root.right.right = BinaryTreeNode(7)

        nodes = root.traverse_inorder()
        values = [n.value for n in nodes]
        assert values == [1, 2, 3, 4, 5, 6, 7]

    def test_traverse_preorder(self):
        """Test pre-order traversal."""
        root = BinaryTreeNode(4)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(6)
        root.left.left = BinaryTreeNode(1)
        root.left.right = BinaryTreeNode(3)

        nodes = root.traverse_preorder()
        values = [n.value for n in nodes]
        assert values == [4, 2, 1, 3, 6]

    def test_traverse_postorder(self):
        """Test post-order traversal."""
        root = BinaryTreeNode(4)
        root.left = BinaryTreeNode(2)
        root.right = BinaryTreeNode(6)
        root.left.left = BinaryTreeNode(1)
        root.left.right = BinaryTreeNode(3)

        nodes = root.traverse_postorder()
        values = [n.value for n in nodes]
        assert values == [1, 3, 2, 6, 4]

    def test_repr(self):
        """Test string representation."""
        node = BinaryTreeNode(42)
        repr_str = repr(node)

        assert "BinaryTreeNode" in repr_str
        assert "value=42" in repr_str
