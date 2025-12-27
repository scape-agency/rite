# -*- coding: utf-8 -*-

"""Tests for PriorityQueue."""

from src.rite.collections.queue import PriorityQueue


class TestPriorityQueue:
    """Test cases for PriorityQueue class."""

    def test_init(self):
        """Test queue initialization."""
        queue = PriorityQueue()
        assert queue.is_empty()
        assert len(queue) == 0

    def test_push(self):
        """Test pushing items."""
        queue = PriorityQueue()
        queue.push("task1", priority=1)

        assert not queue.is_empty()
        assert len(queue) == 1

    def test_push_multiple(self):
        """Test pushing multiple items."""
        queue = PriorityQueue()
        queue.push("task1", priority=3)
        queue.push("task2", priority=1)
        queue.push("task3", priority=2)

        assert len(queue) == 3

    def test_pop_by_priority(self):
        """Test popping returns lowest priority first."""
        queue = PriorityQueue()
        queue.push("low", priority=3)
        queue.push("high", priority=1)
        queue.push("medium", priority=2)

        assert queue.pop() == "high"
        assert queue.pop() == "medium"
        assert queue.pop() == "low"

    def test_pop_empty(self):
        """Test popping from empty queue."""
        queue = PriorityQueue()
        assert queue.pop() is None

    def test_peek(self):
        """Test peeking at highest priority item."""
        queue = PriorityQueue()
        queue.push("task1", priority=3)
        queue.push("task2", priority=1)

        item = queue.peek()
        assert item == "task2"
        assert len(queue) == 2  # Peek doesn't remove

    def test_peek_empty(self):
        """Test peeking at empty queue."""
        queue = PriorityQueue()
        assert queue.peek() is None

    def test_clear(self):
        """Test clearing queue."""
        queue = PriorityQueue()
        queue.push("task1", priority=1)
        queue.push("task2", priority=2)

        queue.clear()
        assert queue.is_empty()
        assert len(queue) == 0

    def test_same_priority(self):
        """Test items with same priority."""
        queue = PriorityQueue()
        queue.push("first", priority=1)
        queue.push("second", priority=1)
        queue.push("third", priority=1)

        # All have same priority, order may vary
        items = [queue.pop(), queue.pop(), queue.pop()]
        assert set(items) == {"first", "second", "third"}

    def test_repr(self):
        """Test string representation."""
        queue = PriorityQueue()
        queue.push("task", priority=1)

        repr_str = repr(queue)
        assert "PriorityQueue" in repr_str
        assert "size=1" in repr_str
