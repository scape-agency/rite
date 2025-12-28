# =============================================================================
# Test: priority_queue
# =============================================================================

"""
Tests for rite.collections.queue.priority_queue.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.collections.queue.priority_queue import PriorityQueue

# =============================================================================
# Test Class: PriorityQueue
# =============================================================================


class TestPriorityQueue:
    """Tests for PriorityQueue class."""

    def test_instantiation(self) -> None:
        """Test PriorityQueue can be instantiated."""
        instance = PriorityQueue()
        assert instance.is_empty()
        assert len(instance) == 0

    def test_push(self) -> None:
        """Test PriorityQueue.push() method."""
        instance = PriorityQueue()
        instance.push("task1", priority=1)

        assert not instance.is_empty()
        assert len(instance) == 1

    def test_pop(self) -> None:
        """Test PriorityQueue.pop() method."""
        instance = PriorityQueue()
        instance.push("low", priority=3)
        instance.push("high", priority=1)
        instance.push("medium", priority=2)

        assert instance.pop() == "high"
        assert instance.pop() == "medium"
        assert instance.pop() == "low"
        assert instance.pop() is None

    def test_peek(self) -> None:
        """Test PriorityQueue.peek() method."""
        instance = PriorityQueue()
        instance.push("task1", priority=3)
        instance.push("task2", priority=1)

        item = instance.peek()
        assert item == "task2"
        assert len(instance) == 2

        empty = PriorityQueue()
        assert empty.peek() is None

    def test_clear(self) -> None:
        """Test PriorityQueue.clear() method."""
        instance = PriorityQueue()
        instance.push("task1", priority=1)
        instance.push("task2", priority=2)

        instance.clear()
        assert instance.is_empty()
        assert len(instance) == 0

    def test_is_empty(self) -> None:
        """Test PriorityQueue.is_empty() method."""
        instance = PriorityQueue()
        assert instance.is_empty() is True

        instance.push("task", priority=1)
        assert instance.is_empty() is False

        # __repr__ smoke test
        repr_str = repr(instance)
        assert "PriorityQueue" in repr_str
