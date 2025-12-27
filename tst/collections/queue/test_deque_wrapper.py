# -*- coding: utf-8 -*-

"""Tests for DequeWrapper."""

from src.rite.collections.queue import DequeWrapper


class TestDequeWrapper:
    """Test cases for DequeWrapper class."""

    def test_init(self):
        """Test deque initialization."""
        deque = DequeWrapper()
        assert deque.is_empty()
        assert len(deque) == 0

    def test_init_with_max_size(self):
        """Test initialization with max size."""
        deque = DequeWrapper(max_size=5)
        assert deque.max_size == 5

    def test_push_right(self):
        """Test pushing to right."""
        deque = DequeWrapper()
        deque.push_right(1)
        deque.push_right(2)

        assert len(deque) == 2
        assert deque.peek_right() == 2

    def test_push_left(self):
        """Test pushing to left."""
        deque = DequeWrapper()
        deque.push_left(1)
        deque.push_left(2)

        assert len(deque) == 2
        assert deque.peek_left() == 2

    def test_pop_right(self):
        """Test popping from right."""
        deque = DequeWrapper()
        deque.push_right(1)
        deque.push_right(2)

        assert deque.pop_right() == 2
        assert deque.pop_right() == 1
        assert deque.is_empty()

    def test_pop_left(self):
        """Test popping from left."""
        deque = DequeWrapper()
        deque.push_right(1)
        deque.push_right(2)

        assert deque.pop_left() == 1
        assert deque.pop_left() == 2
        assert deque.is_empty()

    def test_pop_empty(self):
        """Test popping from empty deque."""
        deque = DequeWrapper()
        assert deque.pop_left() is None
        assert deque.pop_right() is None

    def test_peek_left(self):
        """Test peeking at left."""
        deque = DequeWrapper()
        deque.push_right(1)
        deque.push_right(2)

        assert deque.peek_left() == 1
        assert len(deque) == 2  # Peek doesn't remove

    def test_peek_right(self):
        """Test peeking at right."""
        deque = DequeWrapper()
        deque.push_right(1)
        deque.push_right(2)

        assert deque.peek_right() == 2
        assert len(deque) == 2

    def test_peek_empty(self):
        """Test peeking at empty deque."""
        deque = DequeWrapper()
        assert deque.peek_left() is None
        assert deque.peek_right() is None

    def test_rotate_positive(self):
        """Test rotating right."""
        deque = DequeWrapper()
        for i in range(1, 6):
            deque.push_right(i)

        deque.rotate(2)
        # [1,2,3,4,5] -> [4,5,1,2,3]
        assert deque.pop_left() == 4
        assert deque.pop_left() == 5

    def test_rotate_negative(self):
        """Test rotating left."""
        deque = DequeWrapper()
        for i in range(1, 6):
            deque.push_right(i)

        deque.rotate(-2)
        # [1,2,3,4,5] -> [3,4,5,1,2]
        assert deque.pop_left() == 3
        assert deque.pop_left() == 4

    def test_clear(self):
        """Test clearing deque."""
        deque = DequeWrapper()
        deque.push_right(1)
        deque.push_right(2)

        deque.clear()
        assert deque.is_empty()

    def test_max_size_enforcement(self):
        """Test max size enforcement."""
        deque = DequeWrapper(max_size=3)
        deque.push_right(1)
        deque.push_right(2)
        deque.push_right(3)
        deque.push_right(4)  # Should push out 1

        assert len(deque) == 3
        assert deque.peek_left() == 2

    def test_repr(self):
        """Test string representation."""
        deque = DequeWrapper(max_size=10)
        deque.push_right(1)

        repr_str = repr(deque)
        assert "DequeWrapper" in repr_str
        assert "size=1" in repr_str
