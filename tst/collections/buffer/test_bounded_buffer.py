# -*- coding: utf-8 -*-

"""Tests for BoundedBuffer."""

# Import | Libraries
import pytest

# Import | Local Modules
from src.rite.collections.buffer import BoundedBuffer


class TestBoundedBuffer:
    """Test cases for BoundedBuffer class."""

    def test_init_default(self):
        """Test default initialization."""
        buffer = BoundedBuffer(5)
        assert buffer.capacity == 5
        assert buffer.overflow_strategy == "drop_oldest"
        assert len(buffer) == 0

    def test_init_strategies(self):
        """Test initialization with different strategies."""
        strategies = ["block", "drop_oldest", "drop_newest", "raise"]
        for strategy in strategies:
            buffer = BoundedBuffer(5, overflow_strategy=strategy)
            assert buffer.overflow_strategy == strategy

    def test_init_invalid_strategy(self):
        """Test invalid overflow strategy."""
        with pytest.raises(ValueError, match="Invalid overflow_strategy"):
            BoundedBuffer(5, overflow_strategy="invalid")

    def test_append_drop_oldest(self):
        """Test append with drop_oldest strategy."""
        buffer = BoundedBuffer(3, overflow_strategy="drop_oldest")
        for i in range(5):
            buffer.append(i)

        assert list(buffer) == [2, 3, 4]

    def test_append_drop_newest(self):
        """Test append with drop_newest strategy."""
        buffer = BoundedBuffer(3, overflow_strategy="drop_newest")
        buffer.append(1)
        buffer.append(2)
        buffer.append(3)
        buffer.append(4)  # Should be dropped

        assert list(buffer) == [1, 2, 3]

    def test_append_raise(self):
        """Test append with raise strategy."""
        buffer = BoundedBuffer(3, overflow_strategy="raise")
        buffer.append(1)
        buffer.append(2)
        buffer.append(3)

        with pytest.raises(OverflowError, match="Buffer is full"):
            buffer.append(4)

    def test_append_block(self):
        """Test append with block strategy (should block)."""
        buffer = BoundedBuffer(3, overflow_strategy="block")
        buffer.append(1)
        buffer.append(2)
        buffer.append(3)

        # In single-threaded test, this should block indefinitely
        # We can't easily test this without threading, so just verify setup
        assert buffer.is_full()

    def test_peek(self):
        """Test peeking at oldest item."""
        buffer = BoundedBuffer(5)
        assert buffer.peek() is None

        buffer.append(1)
        buffer.append(2)
        assert buffer.peek() == 1
        assert len(buffer) == 2  # Peek doesn't remove

    def test_get(self):
        """Test getting items by index."""
        buffer = BoundedBuffer(5)
        buffer.append(1)
        buffer.append(2)
        buffer.append(3)

        assert buffer.get(0) == 1
        assert buffer.get(1) == 2
        assert buffer.get(10) is None

    def test_clear(self):
        """Test clearing buffer."""
        buffer = BoundedBuffer(5)
        buffer.append(1)
        buffer.append(2)
        buffer.clear()

        assert len(buffer) == 0
        assert buffer.is_empty()

    def test_is_full(self):
        """Test full status checking."""
        buffer = BoundedBuffer(2)
        assert not buffer.is_full()

        buffer.append(1)
        assert not buffer.is_full()

        buffer.append(2)
        assert buffer.is_full()

    def test_repr(self):
        """Test string representation."""
        buffer = BoundedBuffer(5, overflow_strategy="raise")
        repr_str = repr(buffer)

        assert "BoundedBuffer" in repr_str
        assert "capacity=5" in repr_str
        assert "strategy=raise" in repr_str
