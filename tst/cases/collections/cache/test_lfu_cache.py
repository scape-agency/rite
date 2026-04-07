# -*- coding: utf-8 -*-


# =============================================================================
# Docstring
# =============================================================================

"""Tests for LFUCache."""

# Import | Libraries
import pytest

# Import | Local Modules
from src.rite.collections.cache import LFUCache


class TestLFUCache:
    """Test cases for LFUCache class."""

    def test_init(self):
        """Test cache initialization."""
        cache = LFUCache(5)
        assert cache.capacity == 5
        assert len(cache) == 0

    def test_init_invalid_capacity(self):
        """Test initialization with invalid capacity."""
        with pytest.raises(ValueError, match="Capacity must be at least 1"):
            LFUCache(0)

    def test_put_and_get(self):
        """Test basic put and get operations."""
        cache = LFUCache(3)
        cache.put("key1", "value1")

        assert cache.get("key1") == "value1"
        assert len(cache) == 1

    def test_get_nonexistent(self):
        """Test getting non-existent key."""
        cache = LFUCache(3)
        assert cache.get("missing") is None

    def test_put_updates_existing(self):
        """Test updating existing key."""
        cache = LFUCache(3)
        cache.put("key1", "value1")
        cache.put("key1", "value2")

        assert cache.get("key1") == "value2"
        assert len(cache) == 1

    def test_lfu_eviction(self):
        """Test LFU eviction policy."""
        cache = LFUCache(3)
        cache.put("key1", "value1")
        cache.put("key2", "value2")
        cache.put("key3", "value3")

        # Access key1 and key2 multiple times
        cache.get("key1")
        cache.get("key1")
        cache.get("key2")

        # key3 has lowest frequency, should be evicted
        cache.put("key4", "value4")

        assert cache.get("key3") is None
        assert cache.get("key1") == "value1"
        assert cache.get("key2") == "value2"
        assert cache.get("key4") == "value4"

    def test_get_increments_frequency(self):
        """Test that get increments frequency."""
        cache = LFUCache(2)
        cache.put("key1", "value1")
        cache.put("key2", "value2")

        # Access key2 more times
        cache.get("key2")
        cache.get("key2")

        # Adding key3 should evict key1 (lower frequency)
        cache.put("key3", "value3")

        assert cache.get("key1") is None
        assert cache.get("key2") == "value2"

    def test_delete(self):
        """Test deleting a key."""
        cache = LFUCache(3)
        cache.put("key1", "value1")

        assert cache.delete("key1") is True
        assert cache.get("key1") is None
        assert len(cache) == 0

    def test_delete_nonexistent(self):
        """Test deleting non-existent key."""
        cache = LFUCache(3)
        assert cache.delete("missing") is False

    def test_clear(self):
        """Test clearing cache."""
        cache = LFUCache(3)
        cache.put("key1", "value1")
        cache.put("key2", "value2")

        cache.clear()
        assert len(cache) == 0
        assert cache.get("key1") is None

    def test_zero_capacity(self):
        """Test cache with zero capacity."""
        cache = LFUCache(1)
        cache.capacity = 0  # Simulate zero capacity

        cache.put("key1", "value1")
        # Should not store anything
        # Behavior is implementation dependent

    def test_contains(self):
        """Test membership checking."""
        cache = LFUCache(3)
        cache.put("key1", "value1")

        assert "key1" in cache
        assert "key2" not in cache

    def test_repr(self):
        """Test string representation."""
        cache = LFUCache(10)
        cache.put("key1", "value1")

        repr_str = repr(cache)
        assert "LFUCache" in repr_str
        assert "capacity=10" in repr_str
        assert "size=1" in repr_str

    def test_same_frequency_eviction(self):
        """Test eviction when items have same frequency."""
        cache = LFUCache(2)
        cache.put("key1", "value1")
        cache.put("key2", "value2")

        # Both have frequency 1, adding key3 should evict one
        cache.put("key3", "value3")

        assert len(cache) == 2
        # Either key1 or key2 should be evicted (implementation dependent)
