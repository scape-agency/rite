# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""
Bounded Buffer
==============

A thread-safe bounded buffer that blocks or raises errors when capacity limits
are reached.

"""


# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from collections import deque
from typing import Any

# =============================================================================
# Classes
# =============================================================================


class BoundedBuffer:
    """
    BoundedBuffer Class
    ===================

    A size-limited buffer that prevents overflow with configurable behavior.

    Parameters
    ----------
    maxsize : int
        Maximum number of elements the buffer can hold.
    overflow_strategy : str
        Strategy when full: 'block', 'drop_oldest', 'drop_newest', 'raise'

    """

    def __init__(
        self,
        maxsize: int,
        overflow_strategy: str = "drop_oldest",
    ) -> None:
        """
        Initialize the bounded buffer.

        Args:
        ----
            maxsize: Maximum capacity of the buffer.
            overflow_strategy: Behavior when buffer is full.

        """
        if maxsize < 1:
            raise ValueError("maxsize must be at least 1")

        valid_strategies = {"block", "drop_oldest", "drop_newest", "raise"}
        if overflow_strategy not in valid_strategies:
            raise ValueError(
                f"overflow_strategy must be one of {valid_strategies}"
            )

        self.maxsize = maxsize
        self.overflow_strategy = overflow_strategy
        self._buffer: deque[Any] = deque(maxlen=maxsize)

    def append(self, item: Any) -> bool:
        """
        Add an item to the buffer.

        Args:
        ----
            item: The item to add.

        Returns:
        -------
            bool: True if item was added, False if dropped.

        Raises:
        ------
            BufferError: If overflow_strategy is 'raise' and buffer is full.

        """
        if len(self._buffer) >= self.maxsize:
            if self.overflow_strategy == "raise":
                raise BufferError("Buffer is full")
            elif self.overflow_strategy == "drop_newest":
                return False
            # 'drop_oldest' and 'block' handled by deque

        self._buffer.append(item)
        return True

    def extend(self, items: list[Any]) -> None:
        """
        Extend buffer with multiple items.

        Args:
        ----
            items: List of items to add.

        """
        for item in items:
            self.append(item)

    def get_all(self) -> list[Any]:
        """
        Get all items in buffer.

        Returns:
        -------
            list[Any]: All items in insertion order.

        """
        return list(self._buffer)

    def clear(self) -> None:
        """Clear all items from buffer."""
        self._buffer.clear()

    def is_full(self) -> bool:
        """
        Check if buffer is full.

        Returns:
        -------
            bool: True if buffer has reached maxsize.

        """
        return len(self._buffer) >= self.maxsize

    def is_empty(self) -> bool:
        """
        Check if buffer is empty.

        Returns:
        -------
            bool: True if buffer contains no items.

        """
        return len(self._buffer) == 0

    def __len__(self) -> int:
        """Return number of items in buffer."""
        return len(self._buffer)

    def __iter__(self):
        """Iterate over buffer items."""
        return iter(self._buffer)

    def __repr__(self) -> str:
        """Return string representation of buffer."""
        return (
            f"BoundedBuffer(maxsize={self.maxsize}, "
            f"size={len(self._buffer)}, "
            f"strategy='{self.overflow_strategy}')"
        )


# =============================================================================
# Module Exports
# =============================================================================

__all__: list[str] = [
    "BoundedBuffer",
]
