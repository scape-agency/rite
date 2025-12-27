# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Collections Module
==================

This module provides data structures and utilities for common programming
patterns, organized into logical submodules.

Submodules:
-----------
- buffer: Ring buffers, circular buffers, and sliding windows
- tree: Tree nodes, binary trees, tries, and nested sets
- pattern: Design patterns (singleton, observer, object pool)
- queue: Priority queues, circular queues, and deque wrappers
- cache: LRU, LFU, and TTL caches

Example:
    >>> from rite.collections import CircularBuffer, LRUCache
    >>> buf = CircularBuffer(5)
    >>> cache = LRUCache(100)

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local | Buffer
from .buffer import BoundedBuffer, CircularBuffer, RingBuffer, SlidingWindow

# Import | Local | Cache
from .cache import LFUCache, LRUCache, TTLCache

# Import | Local | Pattern
from .pattern import ObjectPool, Observable, Observer, SingletonMeta

# Import | Local | Queue
from .queue import CircularQueue, DequeWrapper, PriorityQueue

# Import | Local | Tree
from .tree import BinaryTreeNode, NestedSetStructure, TreeNode, Trie

# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    # Buffer
    "CircularBuffer",
    "RingBuffer",
    "BoundedBuffer",
    "SlidingWindow",
    # Tree
    "NestedSetStructure",
    "TreeNode",
    "BinaryTreeNode",
    "Trie",
    # Pattern
    "SingletonMeta",
    "Observer",
    "Observable",
    "ObjectPool",
    # Queue
    "PriorityQueue",
    "DequeWrapper",
    "CircularQueue",
    # Cache
    "LRUCache",
    "LFUCache",
    "TTLCache",
]
