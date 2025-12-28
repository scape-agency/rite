# =============================================================================
# Test: bounded_buffer
# =============================================================================

"""
Tests for rite.collections.buffer.bounded_buffer.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.buffer.bounded_buffer import BoundedBuffer

# =============================================================================
# Test Class
# =============================================================================


class TestBoundedBuffer:
    """Tests for BoundedBuffer class."""

    def test_initialization(self) -> None:
        """Test buffer initialization."""
        buffer = BoundedBuffer(maxsize=5)
        assert buffer.maxsize == 5
        assert buffer.capacity == 5
        assert len(buffer) == 0

    def test_invalid_maxsize(self) -> None:
        """Test that invalid maxsize raises ValueError."""
        with pytest.raises(ValueError, match="maxsize must be at least 1"):
            BoundedBuffer(maxsize=0)
        with pytest.raises(ValueError, match="maxsize must be at least 1"):
            BoundedBuffer(maxsize=-1)

    def test_invalid_overflow_strategy(self) -> None:
        """Test that invalid overflow_strategy raises ValueError."""
        with pytest.raises(ValueError, match="Invalid overflow_strategy"):
            BoundedBuffer(maxsize=5, overflow_strategy="invalid")

    def test_append_and_get_all(self) -> None:
        """Test append and get_all methods."""
        buffer = BoundedBuffer(maxsize=3)
        buffer.append(1)
        buffer.append(2)
        buffer.append(3)
        assert buffer.get_all() == [1, 2, 3]

    def test_overflow_drop_oldest(self) -> None:
        """Test drop_oldest overflow strategy."""
        buffer = BoundedBuffer(maxsize=2, overflow_strategy="drop_oldest")
        buffer.append(1)
        buffer.append(2)
        buffer.append(3)  # Should drop 1
        assert buffer.get_all() == [2, 3]

    def test_overflow_drop_newest(self) -> None:
        """Test drop_newest overflow strategy."""
        buffer = BoundedBuffer(maxsize=2, overflow_strategy="drop_newest")
        buffer.append(1)
        buffer.append(2)
        result = buffer.append(3)  # Should not add
        assert result is False
        assert buffer.get_all() == [1, 2]

    def test_overflow_raise(self) -> None:
        """Test raise overflow strategy."""
        buffer = BoundedBuffer(maxsize=2, overflow_strategy="raise")
        buffer.append(1)
        buffer.append(2)
        with pytest.raises(OverflowError, match="Buffer is full"):
            buffer.append(3)

    def test_peek(self) -> None:
        """Test peek method."""
        buffer = BoundedBuffer(maxsize=3)
        assert buffer.peek() is None
        buffer.append(1)
        buffer.append(2)
        assert buffer.peek() == 1

    def test_get_index(self) -> None:
        """Test get method with index."""
        buffer = BoundedBuffer(maxsize=3)
        buffer.append("a")
        buffer.append("b")
        buffer.append("c")
        assert buffer.get(0) == "a"
        assert buffer.get(1) == "b"
        assert buffer.get(2) == "c"
        assert buffer.get(3) is None  # Out of bounds
        assert buffer.get(-1) is None  # Negative index

    def test_clear(self) -> None:
        """Test clear method."""
        buffer = BoundedBuffer(maxsize=3)
        buffer.append(1)
        buffer.append(2)
        buffer.clear()
        assert len(buffer) == 0
        assert buffer.get_all() == []

    def test_is_full(self) -> None:
        """Test is_full method."""
        buffer = BoundedBuffer(maxsize=2)
        assert not buffer.is_full()
        buffer.append(1)
        assert not buffer.is_full()
        buffer.append(2)
        assert buffer.is_full()

    def test_extend(self) -> None:
        """Test extend method."""
        buffer = BoundedBuffer(maxsize=5)
        buffer.extend([1, 2, 3])
        assert buffer.get_all() == [1, 2, 3]
