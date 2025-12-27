# -*- coding: utf-8 -*-

"""Tests for CircularBuffer."""

import pytest

from src.rite.collections.buffer import CircularBuffer


class TestCircularBuffer:
    """Test cases for CircularBuffer class."""

    def test_init(self):
        """Test buffer initialization."""
        buffer = CircularBuffer(5)
        assert buffer.capacity == 5
        assert len(buffer) == 0
        assert buffer.is_empty()
        assert not buffer.is_full()

    def test_init_invalid_capacity(self):
        """Test initialization with invalid capacity."""
        with pytest.raises(ValueError, match="Capacity must be at least 1"):
            CircularBuffer(0)
        with pytest.raises(ValueError, match="Capacity must be at least 1"):
            CircularBuffer(-1)

    def test_append(self):
        """Test appending items."""
        buffer = CircularBuffer(3)
        buffer.append(1)
        assert len(buffer) == 1
        assert not buffer.is_empty()

        buffer.append(2)
        buffer.append(3)
        assert len(buffer) == 3
        assert buffer.is_full()

    def test_append_overwrites(self):
        """Test that append overwrites oldest item when full."""
        buffer = CircularBuffer(3)
        buffer.append(1)
        buffer.append(2)
        buffer.append(3)
        buffer.append(4)  # Should overwrite 1

        assert len(buffer) == 3
        assert list(buffer) == [2, 3, 4]

    def test_get_valid_index(self):
        """Test getting items by index."""
        buffer = CircularBuffer(5)
        buffer.append(1)
        buffer.append(2)
        buffer.append(3)

        assert buffer.get(0) == 1
        assert buffer.get(1) == 2
        assert buffer.get(2) == 3

    def test_get_invalid_index(self):
        """Test getting with invalid index."""
        buffer = CircularBuffer(5)
        buffer.append(1)

        assert buffer.get(5) is None
        assert buffer.get(-1) is None

    def test_clear(self):
        """Test clearing the buffer."""
        buffer = CircularBuffer(5)
        buffer.append(1)
        buffer.append(2)
        buffer.clear()

        assert len(buffer) == 0
        assert buffer.is_empty()

    def test_iter(self):
        """Test iteration over buffer."""
        buffer = CircularBuffer(5)
        items = [1, 2, 3, 4, 5]
        for item in items:
            buffer.append(item)

        assert list(buffer) == items

    def test_contains(self):
        """Test membership checking."""
        buffer = CircularBuffer(5)
        buffer.append(1)
        buffer.append(2)

        assert 1 in buffer
        assert 2 in buffer
        assert 3 not in buffer

    def test_repr(self):
        """Test string representation."""
        buffer = CircularBuffer(5)
        buffer.append(1)

        repr_str = repr(buffer)
        assert "CircularBuffer" in repr_str
        assert "capacity=5" in repr_str
        assert "size=1" in repr_str

    def test_wrap_around(self):
        """Test buffer wraps around correctly."""
        buffer = CircularBuffer(3)
        for i in range(10):
            buffer.append(i)

        # Should contain last 3 items
        assert list(buffer) == [7, 8, 9]
