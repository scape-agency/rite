# -*- coding: utf-8 -*-

"""Tests for TreeNode."""

# Import | Local Modules
from src.rite.collections.tree import TreeNode


class TestTreeNode:
    """Test cases for TreeNode class."""

    def test_init(self):
        """Test node initialization."""
        node = TreeNode(1)
        assert node.value == 1
        assert not node.children
        assert node.parent is None

    def test_init_with_children(self):
        """Test initialization with children."""
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        parent = TreeNode(1, children=[child1, child2])

        assert len(parent.children) == 2
        assert child1.parent is parent
        assert child2.parent is parent

    def test_add_child(self):
        """Test adding a child."""
        parent = TreeNode(1)
        child = TreeNode(2)
        parent.add_child(child)

        assert child in parent.children
        assert child.parent is parent

    def test_remove_child(self):
        """Test removing a child."""
        parent = TreeNode(1)
        child = TreeNode(2)
        parent.add_child(child)

        result = parent.remove_child(child)
        assert result is True
        assert child not in parent.children
        assert child.parent is None

    def test_remove_nonexistent_child(self):
        """Test removing non-existent child."""
        parent = TreeNode(1)
        child = TreeNode(2)

        result = parent.remove_child(child)
        assert result is False

    def test_is_leaf(self):
        """Test leaf detection."""
        parent = TreeNode(1)
        child = TreeNode(2)

        assert child.is_leaf()
        parent.add_child(child)
        assert not parent.is_leaf()

    def test_is_root(self):
        """Test root detection."""
        parent = TreeNode(1)
        child = TreeNode(2)
        parent.add_child(child)

        assert parent.is_root()
        assert not child.is_root()

    def test_get_depth(self):
        """Test depth calculation."""
        root = TreeNode(1)
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        grandchild = TreeNode(4)

        root.add_child(child1)
        child1.add_child(child2)
        child2.add_child(grandchild)

        assert root.get_depth() == 0
        assert child1.get_depth() == 1
        assert child2.get_depth() == 2
        assert grandchild.get_depth() == 3

    def test_get_height(self):
        """Test height calculation."""
        root = TreeNode(1)
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        grandchild = TreeNode(4)

        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild)

        assert grandchild.get_height() == 0
        assert child1.get_height() == 1
        assert child2.get_height() == 0
        assert root.get_height() == 2

    def test_get_siblings(self):
        """Test getting siblings."""
        parent = TreeNode(1)
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        child3 = TreeNode(4)

        parent.add_child(child1)
        parent.add_child(child2)
        parent.add_child(child3)

        siblings = child1.get_siblings()
        assert len(siblings) == 2
        assert child2 in siblings
        assert child3 in siblings
        assert child1 not in siblings

    def test_get_siblings_root(self):
        """Test root node has no siblings."""
        root = TreeNode(1)
        assert root.get_siblings() == []

    def test_get_ancestors(self):
        """Test getting ancestors."""
        root = TreeNode(1)
        child = TreeNode(2)
        grandchild = TreeNode(3)

        root.add_child(child)
        child.add_child(grandchild)

        ancestors = grandchild.get_ancestors()
        assert len(ancestors) == 2
        assert ancestors[0] is child
        assert ancestors[1] is root

    def test_get_ancestors_root(self):
        """Test root has no ancestors."""
        root = TreeNode(1)
        assert not root.get_ancestors()

    def test_traverse_preorder(self):
        """Test pre-order traversal."""
        root = TreeNode(1)
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        grandchild1 = TreeNode(4)
        grandchild2 = TreeNode(5)

        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild1)
        child1.add_child(grandchild2)

        nodes = root.traverse_preorder()
        values = [n.value for n in nodes]
        assert values == [1, 2, 4, 5, 3]

    def test_traverse_postorder(self):
        """Test post-order traversal."""
        root = TreeNode(1)
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        grandchild1 = TreeNode(4)
        grandchild2 = TreeNode(5)

        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild1)
        child1.add_child(grandchild2)

        nodes = root.traverse_postorder()
        values = [n.value for n in nodes]
        assert values == [4, 5, 2, 3, 1]

    def test_traverse_levelorder(self):
        """Test level-order traversal."""
        root = TreeNode(1)
        child1 = TreeNode(2)
        child2 = TreeNode(3)
        grandchild1 = TreeNode(4)
        grandchild2 = TreeNode(5)

        root.add_child(child1)
        root.add_child(child2)
        child1.add_child(grandchild1)
        child1.add_child(grandchild2)

        nodes = root.traverse_levelorder()
        values = [n.value for n in nodes]
        assert values == [1, 2, 3, 4, 5]

    def test_repr(self):
        """Test string representation."""
        node = TreeNode(42)
        child = TreeNode(1)
        node.add_child(child)

        repr_str = repr(node)
        assert "TreeNode" in repr_str
        assert "value=42" in repr_str
        assert "children=1" in repr_str
