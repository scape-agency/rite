# =============================================================================
# Test: object_pool
# =============================================================================

"""
Tests for rite.collections.pattern.object_pool.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.pattern.object_pool import (
    ObjectPool,
)

# =============================================================================
# Test Class: ObjectPool
# =============================================================================


class TestObjectPool:
    """Tests for ObjectPool class."""

    def test_instantiation(self) -> None:
        """Test ObjectPool can be instantiated."""
        instance = ObjectPool(factory=lambda: {})
        assert instance is not None
        assert instance.max_size == 10

    def test_acquire(self) -> None:
        """Test ObjectPool.acquire() method."""
        instance = ObjectPool(factory=lambda: {"count": 0})
        obj = instance.acquire()
        assert obj is not None
        assert isinstance(obj, dict)
        assert instance.in_use_count() == 1

    def test_release(self) -> None:
        """Test ObjectPool.release() method."""
        instance = ObjectPool(factory=lambda: {"count": 0})
        obj = instance.acquire()
        instance.release(obj)
        assert instance.available_count() == 1
        assert instance.in_use_count() == 0

    def test_clear(self) -> None:
        """Test ObjectPool.clear() method."""
        instance = ObjectPool(factory=lambda: {})
        obj = instance.acquire()
        instance.release(obj)
        instance.clear()
        assert instance.available_count() == 0

    def test_size(self) -> None:
        """Test ObjectPool.size() method."""
        instance = ObjectPool(factory=lambda: {})
        assert instance.size() == 0
        obj = instance.acquire()
        assert instance.size() == 1
        instance.release(obj)
        assert instance.size() == 1

    def test_available_count(self) -> None:
        """Test ObjectPool.available_count() method."""
        instance = ObjectPool(factory=lambda: {})
        assert instance.available_count() == 0
        obj = instance.acquire()
        assert instance.available_count() == 0
        instance.release(obj)
        assert instance.available_count() == 1

    def test_in_use_count(self) -> None:
        """Test ObjectPool.in_use_count() method."""
        instance = ObjectPool(factory=lambda: {})
        assert instance.in_use_count() == 0
        obj = instance.acquire()
        assert instance.in_use_count() == 1
        instance.release(obj)
        assert instance.in_use_count() == 0
