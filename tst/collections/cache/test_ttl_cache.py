# -*- coding: utf-8 -*-

"""Tests for TTLCache."""

import time

import pytest

from src.rite.collections.cache import TTLCache


class TestTTLCache:
    """Test cases for TTLCache class."""

    def test_init(self):
        """Test cache initialization."""
        cache = TTLCache(default_ttl=10.0)
        assert cache.default_ttl == 10.0
        assert cache.max_size is None
        assert len(cache) == 0

    def test_init_with_max_size(self):
        """Test initialization with max size."""
        cache = TTLCache(default_ttl=10.0, max_size=5)
        assert cache.max_size == 5

    def test_init_invalid_ttl(self):
        """Test initialization with invalid TTL."""
        with pytest.raises(ValueError, match="TTL must be positive"):
            TTLCache(default_ttl=0)

        with pytest.raises(ValueError, match="TTL must be positive"):
            TTLCache(default_ttl=-1)

    def test_put_and_get(self):
        """Test basic put and get operations."""
        cache = TTLCache(default_ttl=10.0)
        cache.put("key1", "value1")

        assert cache.get("key1") == "value1"
        assert len(cache) == 1

    def test_get_nonexistent(self):
        """Test getting non-existent key."""
        cache = TTLCache(default_ttl=10.0)
        assert cache.get("missing") is None

    def test_put_with_custom_ttl(self):
        """Test putting with custom TTL."""
        cache = TTLCache(default_ttl=10.0)
        cache.put("key1", "value1", ttl=5.0)

        assert cache.get("key1") == "value1"

    def test_expiration(self):
        """Test that items expire after TTL."""
        cache = TTLCache(default_ttl=0.1)  # 100ms TTL
        cache.put("key1", "value1")

        # Should exist immediately
        assert cache.get("key1") == "value1"

        # Wait for expiration
        time.sleep(0.15)

        # Should be expired
        assert cache.get("key1") is None

    def test_custom_ttl_expiration(self):
        """Test expiration with custom TTL."""
        cache = TTLCache(default_ttl=10.0)
        cache.put("key1", "value1", ttl=0.1)

        assert cache.get("key1") == "value1"

        time.sleep(0.15)
        assert cache.get("key1") is None

    def test_delete(self):
        """Test deleting a key."""
        cache = TTLCache(default_ttl=10.0)
        cache.put("key1", "value1")

        assert cache.delete("key1") is True
        assert cache.get("key1") is None

    def test_delete_nonexistent(self):
        """Test deleting non-existent key."""
        cache = TTLCache(default_ttl=10.0)
        assert cache.delete("missing") is False

    def test_clear(self):
        """Test clearing cache."""
        cache = TTLCache(default_ttl=10.0)
        cache.put("key1", "value1")
        cache.put("key2", "value2")

        cache.clear()
        assert len(cache) == 0

    def test_get_ttl(self):
        """Test getting remaining TTL."""
        cache = TTLCache(default_ttl=10.0)
        cache.put("key1", "value1")

        ttl = cache.get_ttl("key1")
        assert ttl is not None
        assert 9.0 < ttl <= 10.0

    def test_get_ttl_nonexistent(self):
        """Test getting TTL for non-existent key."""
        cache = TTLCache(default_ttl=10.0)
        assert cache.get_ttl("missing") is None

    def test_get_ttl_expired(self):
        """Test getting TTL for expired key."""
        cache = TTLCache(default_ttl=0.1)
        cache.put("key1", "value1")

        time.sleep(0.15)
        assert cache.get_ttl("key1") is None

    def test_max_size_enforcement(self):
        """Test max size enforcement."""
        cache = TTLCache(default_ttl=10.0, max_size=2)
        cache.put("key1", "value1")
        cache.put("key2", "value2")
        cache.put("key3", "value3")  # Should trigger cleanup

        # Should have at most 2 items
        assert len(cache) <= 2

    def test_max_size_with_expiration(self):
        """Test max size with expired items."""
        cache = TTLCache(default_ttl=0.1, max_size=2)
        cache.put("key1", "value1")
        cache.put("key2", "value2")

        # Wait for expiration
        time.sleep(0.15)

        # Add new item, should cleanup expired
        cache.put("key3", "value3")
        assert cache.get("key3") == "value3"
        assert len(cache) == 1  # Only key3 should remain

    def test_contains(self):
        """Test membership checking."""
        cache = TTLCache(default_ttl=10.0)
        cache.put("key1", "value1")

        assert "key1" in cache
        assert "key2" not in cache

    def test_contains_expired(self):
        """Test membership with expired item."""
        cache = TTLCache(default_ttl=0.1)
        cache.put("key1", "value1")

        time.sleep(0.15)
        assert "key1" not in cache

    def test_repr(self):
        """Test string representation."""
        cache = TTLCache(default_ttl=5.0)
        cache.put("key1", "value1")

        repr_str = repr(cache)
        assert "TTLCache" in repr_str
        assert "default_ttl=5.0" in repr_str
        assert "size=1" in repr_str
