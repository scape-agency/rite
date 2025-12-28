# =============================================================================
# Test: deque_wrapper
# =============================================================================

"""
Tests for rite.collections.queue.deque_wrapper.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.collections.queue.deque_wrapper import DequeWrapper

# =============================================================================
# Test Class: DequeWrapper
# =============================================================================


class TestDequeWrapper:
    """Tests for DequeWrapper class."""

    def test_instantiation(self) -> None:
        """Test DequeWrapper can be instantiated."""
        instance = DequeWrapper()
        assert instance.is_empty()
        assert len(instance) == 0

    def test_push_left(self) -> None:
        """Test DequeWrapper.push_left() method."""
        instance = DequeWrapper()
        instance.push_left(1)
        instance.push_left(2)

        assert len(instance) == 2
        assert instance.peek_left() == 2

    def test_push_right(self) -> None:
        """Test DequeWrapper.push_right() method."""
        instance = DequeWrapper()
        instance.push_right(1)
        instance.push_right(2)

        assert len(instance) == 2
        assert instance.peek_right() == 2

    def test_pop_left(self) -> None:
        """Test DequeWrapper.pop_left() method."""
        instance = DequeWrapper()
        instance.push_right(1)
        instance.push_right(2)

        assert instance.pop_left() == 1
        assert instance.pop_left() == 2
        assert instance.is_empty()

    def test_pop_right(self) -> None:
        """Test DequeWrapper.pop_right() method."""
        instance = DequeWrapper()
        instance.push_right(1)
        instance.push_right(2)

        assert instance.pop_right() == 2
        assert instance.pop_right() == 1
        assert instance.is_empty()

    def test_peek_left(self) -> None:
        """Test DequeWrapper.peek_left() method."""
        instance = DequeWrapper()
        instance.push_right(1)
        instance.push_right(2)

        assert instance.peek_left() == 1
        assert len(instance) == 2

    def test_peek_right(self) -> None:
        """Test DequeWrapper.peek_right() method."""
        instance = DequeWrapper()
        instance.push_right(1)
        instance.push_right(2)

        assert instance.peek_right() == 2
        assert len(instance) == 2

    def test_rotate(self) -> None:
        """Test DequeWrapper.rotate() method."""
        instance = DequeWrapper()
        for i in range(1, 6):
            instance.push_right(i)

        instance.rotate(2)
        assert instance.pop_left() == 4
        assert instance.pop_left() == 5

        # Negative rotation
        instance = DequeWrapper()
        for i in range(1, 6):
            instance.push_right(i)
        instance.rotate(-2)
        assert instance.pop_left() == 3
        assert instance.pop_left() == 4

    def test_clear(self) -> None:
        """Test DequeWrapper.clear() method."""
        instance = DequeWrapper()
        instance.push_right(1)
        instance.push_right(2)

        instance.clear()
        assert instance.is_empty()

    def test_is_empty(self) -> None:
        """Test DequeWrapper.is_empty() method."""
        instance = DequeWrapper()
        assert instance.is_empty() is True

        instance.push_right(1)
        assert instance.is_empty() is False

    def test_to_list(self) -> None:
        """Test DequeWrapper.to_list() method."""
        instance = DequeWrapper()
        instance.push_right(1)
        instance.push_right(2)

        assert instance.to_list() == [1, 2]

        # __repr__ smoke test
        repr_str = repr(instance)
        assert "DequeWrapper" in repr_str
