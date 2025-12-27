# -*- coding: utf-8 -*-

"""Tests for CircularQueue."""

# Import | Libraries
import pytest

# Import | Local Modules
from src.rite.collections.queue import CircularQueue


class TestCircularQueue:
    """Test cases for CircularQueue class."""

    def test_init(self):
        """Test queue initialization."""
        queue = CircularQueue(5)
        assert queue.capacity == 5
        assert queue.is_empty()
        assert not queue.is_full()
        assert len(queue) == 0

    def test_init_invalid_capacity(self):
        """Test initialization with invalid capacity."""
        with pytest.raises(ValueError, match="Capacity must be at least 1"):
            CircularQueue(0)

    def test_enqueue(self):
        """Test enqueueing items."""
        queue = CircularQueue(3)
        queue.enqueue(1)
        queue.enqueue(2)

        assert len(queue) == 2
        assert not queue.is_empty()
        assert not queue.is_full()

    def test_enqueue_full(self):
        """Test enqueueing when full."""
        queue = CircularQueue(2)
        queue.enqueue(1)
        queue.enqueue(2)

        with pytest.raises(OverflowError, match="Queue is full"):
            queue.enqueue(3)

    def test_dequeue(self):
        """Test dequeueing items."""
        queue = CircularQueue(5)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert len(queue) == 1

    def test_dequeue_empty(self):
        """Test dequeueing from empty queue."""
        queue = CircularQueue(5)

        with pytest.raises(IndexError, match="Queue is empty"):
            queue.dequeue()

    def test_peek(self):
        """Test peeking at front item."""
        queue = CircularQueue(5)
        queue.enqueue(1)
        queue.enqueue(2)

        assert queue.peek() == 1
        assert len(queue) == 2  # Peek doesn't remove

    def test_peek_empty(self):
        """Test peeking at empty queue."""
        queue = CircularQueue(5)
        assert queue.peek() is None

    def test_clear(self):
        """Test clearing queue."""
        queue = CircularQueue(5)
        queue.enqueue(1)
        queue.enqueue(2)

        queue.clear()
        assert queue.is_empty()
        assert len(queue) == 0

    def test_is_full(self):
        """Test full status checking."""
        queue = CircularQueue(2)
        assert not queue.is_full()

        queue.enqueue(1)
        assert not queue.is_full()

        queue.enqueue(2)
        assert queue.is_full()

    def test_circular_behavior(self):
        """Test circular wrapping behavior."""
        queue = CircularQueue(3)

        # Fill queue
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        # Remove and add (should wrap around)
        assert queue.dequeue() == 1
        queue.enqueue(4)

        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4

    def test_multiple_cycles(self):
        """Test multiple enqueue/dequeue cycles."""
        queue = CircularQueue(3)

        for i in range(10):
            queue.enqueue(i)
            assert queue.dequeue() == i

        assert queue.is_empty()

    def test_repr(self):
        """Test string representation."""
        queue = CircularQueue(5)
        queue.enqueue(1)

        repr_str = repr(queue)
        assert "CircularQueue" in repr_str
        assert "capacity=5" in repr_str
        assert "size=1" in repr_str
