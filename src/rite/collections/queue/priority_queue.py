# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Priority Queue
==============

A priority queue implementation using heapq.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import heapq
from typing import Any

# =============================================================================
# Classes
# =============================================================================


class PriorityQueue:
    """
    PriorityQueue Class
    ===================

    A priority queue where items with lower priority values are dequeued first.

    """

    def __init__(self) -> None:
        """Initialize an empty priority queue."""
        self._heap: list[tuple[float, int, Any]] = []
        self._counter = 0  # For stable sorting

    def push(self, item: Any, priority: float = 0.0) -> None:
        """
        Add an item with a given priority.

        Args:
        ----
            item: The item to add.
            priority: Priority value (lower = higher priority).

        """
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1

    def pop(self) -> Any:
        """
        Remove and return the highest priority item.

        Returns:
        -------
            Any: The highest priority item.

        Raises:
        ------
            IndexError: If queue is empty.

        """
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        return heapq.heappop(self._heap)[2]

    def peek(self) -> Any:
        """
        Return the highest priority item without removing it.

        Returns:
        -------
            Any: The highest priority item.

        Raises:
        ------
            IndexError: If queue is empty.

        """
        if self.is_empty():
            raise IndexError("peek at empty priority queue")
        return self._heap[0][2]

    def is_empty(self) -> bool:
        """
        Check if queue is empty.

        Returns:
        -------
            bool: True if queue is empty.

        """
        return len(self._heap) == 0

    def __len__(self) -> int:
        """Return number of items in queue."""
        return len(self._heap)

    def __repr__(self) -> str:
        """Return string representation."""
        return f"PriorityQueue(size={len(self._heap)})"


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "PriorityQueue",
]
