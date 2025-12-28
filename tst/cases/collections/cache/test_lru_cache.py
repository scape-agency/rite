# -*- coding: utf-8 -*-

"""Tests for LRUCache."""

# Import | Libraries
import pytest

# Import | Local Modules
from src.rite.collections.cache import LRUCache


class TestLRUCache:
    """Test cases for LRUCache class."""

    def test_init(self):
        """Test cache initialization."""
        cache = LRUCache(5)
        assert cache.capacity == 5
        assert len(cache) == 0

    def test_init_invalid_capacity(self):
        """Test initialization with invalid capacity."""
        with pytest.raises(ValueError, match="Capacity must be at least 1"):
            LRUCache(0)

    def test_put_and_get(self):
        """Test basic put and get operations."""
        cache = LRUCache(3)
        cache.put("key1", "value1")

        assert cache.get("key1") == "value1"
        assert len(cache) == 1

    def test_get_nonexistent(self):
        """Test getting non-existent key."""
        cache = LRUCache(3)
        assert cache.get("missing") is None

    def test_put_updates_existing(self):
        """Test updating existing key."""
        cache = LRUCache(3)
        cache.put("key1", "value1")
        cache.put("key1", "value2")

        assert cache.get("key1") == "value2"
        assert len(cache) == 1

    def test_lru_eviction(self):
        """Test LRU eviction policy."""
        cache = LRUCache(3)
        cache.put("key1", "value1")
        cache.put("key2", "value2")
        cache.put("key3", "value3")
        cache.put("key4", "value4")  # Should evict key1

        assert cache.get("key1") is None
        assert cache.get("key2") == "value2"
        assert cache.get("key3") == "value3"
        assert cache.get("key4") == "value4"

    def test_get_updates_recency(self):
        """Test that get updates recency."""
        cache = LRUCache(3)
        cache.put("key1", "value1")
        cache.put("key2", "value2")
        cache.put("key3", "value3")

        # Access key1 to make it recently used
        cache.get("key1")

        # Add key4, should evict key2 (least recently used)
        cache.put("key4", "value4")

        assert cache.get("key1") == "value1"
        assert cache.get("key2") is None
        assert cache.get("key3") == "value3"
        assert cache.get("key4") == "value4"

    def test_delete(self):
        """Test deleting a key."""
        cache = LRUCache(3)
        cache.put("key1", "value1")

        assert cache.delete("key1") is True
        assert cache.get("key1") is None
        assert len(cache) == 0

    def test_delete_nonexistent(self):
        """Test deleting non-existent key."""
        cache = LRUCache(3)
        assert cache.delete("missing") is False

    def test_clear(self):
        """Test clearing cache."""
        cache = LRUCache(3)
        cache.put("key1", "value1")
        cache.put("key2", "value2")

        cache.clear()
        assert len(cache) == 0
        assert cache.get("key1") is None

    def test_keys(self):
        """Test getting all keys."""
        cache = LRUCache(5)
        cache.put("key1", "value1")
        cache.put("key2", "value2")
        cache.put("key3", "value3")

        keys = cache.keys()
        assert set(keys) == {"key1", "key2", "key3"}

    def test_values(self):
        """Test getting all values."""
        cache = LRUCache(5)
        cache.put("key1", "value1")
        cache.put("key2", "value2")

        values = cache.values()
        assert set(values) == {"value1", "value2"}

    def test_items(self):
        """Test getting all items."""
        cache = LRUCache(5)
        cache.put("key1", "value1")
        cache.put("key2", "value2")

        items = cache.items()
        assert set(items) == {("key1", "value1"), ("key2", "value2")}

    def test_contains(self):
        """Test membership checking."""
        cache = LRUCache(3)
        cache.put("key1", "value1")

        assert "key1" in cache
        assert "key2" not in cache

    def test_repr(self):
        """Test string representation."""
        cache = LRUCache(10)
        cache.put("key1", "value1")

        repr_str = repr(cache)
        assert "LRUCache" in repr_str
        assert "capacity=10" in repr_str
        assert "size=1" in repr_str
