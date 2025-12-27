# -*- coding: utf-8 -*-

"""Tests for SlidingWindow."""

# Import | Libraries
import pytest

# Import | Local Modules
from src.rite.collections.buffer import SlidingWindow


class TestSlidingWindow:
    """Test cases for SlidingWindow class."""

    def test_init(self):
        """Test initialization."""
        window = SlidingWindow(5)
        assert window.size == 5
        assert len(window) == 0
        assert window.is_empty()

    def test_init_invalid_size(self):
        """Test invalid size."""
        with pytest.raises(ValueError, match="Size must be at least 1"):
            SlidingWindow(0)

    def test_add(self):
        """Test adding items."""
        window = SlidingWindow(3)
        window.add(1)
        window.add(2)
        window.add(3)

        assert len(window) == 3
        assert window.is_full()

    def test_add_overflow(self):
        """Test adding beyond capacity."""
        window = SlidingWindow(3)
        for i in range(5):
            window.add(i)

        assert list(window) == [2, 3, 4]

    def test_get_window(self):
        """Test getting window items."""
        window = SlidingWindow(5)
        window.add(1)
        window.add(2)

        assert window.get_window() == [1, 2]

    def test_clear(self):
        """Test clearing window."""
        window = SlidingWindow(5)
        window.add(1)
        window.add(2)
        window.clear()

        assert len(window) == 0
        assert window.is_empty()

    def test_moving_average_empty(self):
        """Test moving average on empty window."""
        window = SlidingWindow(5)
        assert window.moving_average() is None

    def test_moving_average(self):
        """Test moving average calculation."""
        window = SlidingWindow(4)
        window.add(2)
        window.add(4)
        window.add(6)
        window.add(8)

        assert window.moving_average() == 5.0

    def test_moving_sum_empty(self):
        """Test moving sum on empty window."""
        window = SlidingWindow(5)
        assert window.moving_sum() is None

    def test_moving_sum(self):
        """Test moving sum calculation."""
        window = SlidingWindow(3)
        window.add(1)
        window.add(2)
        window.add(3)

        assert window.moving_sum() == 6

    def test_moving_max_empty(self):
        """Test moving max on empty window."""
        window = SlidingWindow(5)
        assert window.moving_max() is None

    def test_moving_max(self):
        """Test moving max calculation."""
        window = SlidingWindow(4)
        window.add(3)
        window.add(1)
        window.add(4)
        window.add(2)

        assert window.moving_max() == 4

    def test_moving_min_empty(self):
        """Test moving min on empty window."""
        window = SlidingWindow(5)
        assert window.moving_min() is None

    def test_moving_min(self):
        """Test moving min calculation."""
        window = SlidingWindow(4)
        window.add(3)
        window.add(1)
        window.add(4)
        window.add(2)

        assert window.moving_min() == 1

    def test_aggregation_with_strings(self):
        """Test aggregation fails gracefully with non-numeric types."""
        window = SlidingWindow(3)
        window.add("a")
        window.add("b")

        # These should handle type errors gracefully
        # Implementation dependent - might return None or raise
        try:
            result = window.moving_average()
            assert result is None or isinstance(result, (int, float))
        except TypeError:
            pass  # Also acceptable

    def test_repr(self):
        """Test string representation."""
        window = SlidingWindow(5)
        window.add(1)

        repr_str = repr(window)
        assert "SlidingWindow" in repr_str
        assert "size=5" in repr_str
