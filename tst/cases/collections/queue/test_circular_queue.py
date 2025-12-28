# =============================================================================
# Test: circular_queue
# =============================================================================

"""
Tests for rite.collections.queue.circular_queue.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.queue.circular_queue import (
    CircularQueue,
)

# =============================================================================
# Test Class: CircularQueue
# =============================================================================


class TestCircularQueue:
    """Tests for CircularQueue class."""

    def test_instantiation(self) -> None:
        """Test CircularQueue can be instantiated."""
        instance = CircularQueue(capacity=5)
        assert instance is not None
        assert instance.capacity == 5
        assert len(instance) == 0

    def test_enqueue(self) -> None:
        """Test CircularQueue.enqueue() method."""
        instance = CircularQueue(capacity=3)
        assert instance.enqueue("a") is True
        assert instance.enqueue("b") is True
        assert len(instance) == 2

    def test_dequeue(self) -> None:
        """Test CircularQueue.dequeue() method."""
        instance = CircularQueue(capacity=3)
        instance.enqueue("a")
        instance.enqueue("b")
        result = instance.dequeue()
        assert result == "a"
        assert len(instance) == 1

    def test_peek(self) -> None:
        """Test CircularQueue.peek() method."""
        instance = CircularQueue(capacity=3)
        assert instance.peek() is None
        instance.enqueue("a")
        instance.enqueue("b")
        assert instance.peek() == "a"
        assert len(instance) == 2

    def test_is_empty(self) -> None:
        """Test CircularQueue.is_empty() method."""
        instance = CircularQueue(capacity=3)
        assert instance.is_empty() is True
        instance.enqueue("a")
        assert instance.is_empty() is False

    def test_is_full(self) -> None:
        """Test CircularQueue.is_full() method."""
        instance = CircularQueue(capacity=2)
        assert instance.is_full() is False
        instance.enqueue("a")
        instance.enqueue("b")
        assert instance.is_full() is True

    def test_clear(self) -> None:
        """Test CircularQueue.clear() method."""
        instance = CircularQueue(capacity=3)
        instance.enqueue("a")
        instance.enqueue("b")
        instance.clear()
        assert len(instance) == 0
        assert instance.is_empty() is True
