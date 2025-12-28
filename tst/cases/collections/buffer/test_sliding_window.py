# =============================================================================
# Test: sliding_window
# =============================================================================

"""
Tests for rite.collections.buffer.sliding_window.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.collections.buffer.sliding_window import SlidingWindow

# =============================================================================
# Test Class
# =============================================================================


class TestSlidingWindow:
    """Tests for SlidingWindow class."""

    def test_initialization(self) -> None:
        """Test window initialization."""
        window = SlidingWindow(size=5)
        assert window.size == 5
        assert len(window) == 0

    def test_add_values(self) -> None:
        """Test adding values to window."""
        window = SlidingWindow(size=3)
        window.add(1)
        window.add(2)
        window.add(3)
        assert window.get_window() == [1, 2, 3]

    def test_sliding_behavior(self) -> None:
        """Test that window slides when full."""
        window = SlidingWindow(size=2)
        window.add(1)
        window.add(2)
        window.add(3)  # Should slide out 1
        assert window.get_window() == [2, 3]

    def test_aggregation_function(self) -> None:
        """Test aggregation function."""
        window = SlidingWindow(size=3, aggregation_func=sum)
        window.add(1)
        result = window.add(2)
        assert result is None  # Not full yet
        result = window.add(3)
        assert result == 6  # Sum of [1, 2, 3]

    def test_get_aggregate(self) -> None:
        """Test get_aggregate method."""
        window = SlidingWindow(size=3, aggregation_func=sum)
        window.add(1)
        window.add(2)
        assert window.get_aggregate() == 3
        window.add(3)
        assert window.get_aggregate() == 6

    def test_get_aggregate_no_func(self) -> None:
        """Test get_aggregate without aggregation function."""
        window = SlidingWindow(size=3)
        window.add(1)
        assert window.get_aggregate() is None

    def test_get_aggregate_empty_window(self) -> None:
        """Test get_aggregate with empty window."""
        window = SlidingWindow(size=3, aggregation_func=sum)
        assert window.get_aggregate() is None

    def test_is_full(self) -> None:
        """Test is_full method."""
        window = SlidingWindow(size=2)
        assert not window.is_full()
        window.add(1)
        assert not window.is_full()
        window.add(2)
        assert window.is_full()

    def test_clear(self) -> None:
        """Test clear method."""
        window = SlidingWindow(size=3)
        window.add(1)
        window.add(2)
        window.clear()
        assert len(window) == 0
        assert window.get_window() == []
