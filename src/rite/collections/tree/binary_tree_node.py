# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Binary Tree Node
================

Binary tree node with left and right children.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from typing import Any

# =============================================================================
# Classes
# =============================================================================


class BinaryTreeNode:
    """
    BinaryTreeNode Class
    ====================

    A binary tree node with left and right children.

    Parameters
    ----------
    value : Any
        The value stored in this node.
    left : BinaryTreeNode | None
        Left child node.
    right : BinaryTreeNode | None
        Right child node.

    """

    def __init__(
        self,
        value: Any,
        left: BinaryTreeNode | None = None,
        right: BinaryTreeNode | None = None,
    ) -> None:
        """
        Initialize a binary tree node.

        Args:
        ----
            value: The value to store.
            left: Left child node.
            right: Right child node.

        """
        self.value = value
        self.left = left
        self.right = right

    def is_leaf(self) -> bool:
        """
        Check if node is a leaf.

        Returns:
        -------
            bool: True if node has no children.

        """
        return self.left is None and self.right is None

    def has_left(self) -> bool:
        """
        Check if node has left child.

        Returns:
        -------
            bool: True if left child exists.

        """
        return self.left is not None

    def has_right(self) -> bool:
        """
        Check if node has right child.

        Returns:
        -------
            bool: True if right child exists.

        """
        return self.right is not None

    def get_height(self) -> int:
        """
        Get height of subtree rooted at this node.

        Returns:
        -------
            int: Height of subtree.

        """
        if self.is_leaf():
            return 0

        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        return 1 + max(left_height, right_height)

    def inorder_traversal(self) -> list[Any]:
        """
        Perform in-order traversal (left, root, right).

        Returns:
        -------
            list[Any]: Values in in-order.

        """
        result = []
        if self.left:
            result.extend(self.left.inorder_traversal())
        result.append(self.value)
        if self.right:
            result.extend(self.right.inorder_traversal())
        return result

    def preorder_traversal(self) -> list[Any]:
        """
        Perform pre-order traversal (root, left, right).

        Returns:
        -------
            list[Any]: Values in pre-order.

        """
        result = [self.value]
        if self.left:
            result.extend(self.left.preorder_traversal())
        if self.right:
            result.extend(self.right.preorder_traversal())
        return result

    def postorder_traversal(self) -> list[Any]:
        """
        Perform post-order traversal (left, right, root).

        Returns:
        -------
            list[Any]: Values in post-order.

        """
        result = []
        if self.left:
            result.extend(self.left.postorder_traversal())
        if self.right:
            result.extend(self.right.postorder_traversal())
        result.append(self.value)
        return result

    def __repr__(self) -> str:
        """Return string representation."""
        return (
            f"BinaryTreeNode(value={self.value}, "
            f"left={'Yes' if self.left else 'No'}, "
            f"right={'Yes' if self.right else 'No'})"
        )


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "BinaryTreeNode",
]
