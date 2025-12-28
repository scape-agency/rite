# -*- coding: utf-8 -*-

"""Tests for ObjectPool."""

# Import | Standard Library
from functools import partial

# Import | Libraries
import pytest

# Import | Local Modules
from src.rite.collections.pattern import ObjectPool


class PoolableObject:
    """Simple object for pooling."""

    def __init__(self, value):
        self.value = value
        self.reset_called = False

    def reset(self):
        """Reset method for pool."""
        self.reset_called = True
        self.value = 0


def make_poolable(value: int = 0) -> PoolableObject:
    """Factory helper for pool tests."""
    return PoolableObject(value)


class TestObjectPool:
    """Test cases for ObjectPool class."""

    def test_init(self):
        """Test pool initialization."""
        pool = ObjectPool(make_poolable, max_size=5)
        assert pool.max_size == 5
        assert pool.available_count() == 0

    def test_init_invalid_max_size(self):
        """Test initialization with invalid max size."""
        with pytest.raises(ValueError, match="max_size must be at least 1"):
            ObjectPool(object, max_size=0)

    def test_acquire(self):
        """Test acquiring object from pool."""
        pool = ObjectPool(partial(make_poolable, 1), max_size=5)

        obj = pool.acquire()
        assert isinstance(obj, PoolableObject)
        assert obj.value == 1

    def test_acquire_multiple(self):
        """Test acquiring multiple objects."""
        pool = ObjectPool(make_poolable, max_size=5)

        obj1 = pool.acquire()
        obj2 = pool.acquire()

        assert obj1 is not obj2

    def test_release(self):
        """Test releasing object back to pool."""
        pool = ObjectPool(make_poolable, max_size=5)

        obj = pool.acquire()
        pool.release(obj)

        assert pool.available_count() == 1

    def test_release_calls_reset(self):
        """Test that release calls reset function."""

        def reset_fn(obj):
            obj.reset()

        pool = ObjectPool(make_poolable, max_size=5, reset=reset_fn)

        obj = pool.acquire()
        assert not obj.reset_called

        pool.release(obj)
        assert obj.reset_called
        assert obj.value == 0

    def test_release_exceeds_max_size(self):
        """Test that release discards when pool is full."""
        pool = ObjectPool(make_poolable, max_size=2)

        obj1 = pool.acquire()
        obj2 = pool.acquire()
        obj3 = pool.acquire()

        pool.release(obj1)
        pool.release(obj2)
        pool.release(obj3)  # Should be discarded

        assert pool.available_count() == 2

    def test_reuse_released_object(self):
        """Test that released objects are reused."""
        pool = ObjectPool(make_poolable, max_size=5)

        obj1 = pool.acquire()
        obj1.value = 42
        pool.release(obj1)

        obj2 = pool.acquire()
        # Should be the same object
        assert obj2 is obj1

    def test_available_count(self):
        """Test available count tracking."""
        pool = ObjectPool(make_poolable, max_size=5)

        assert pool.available_count() == 0

        obj1 = pool.acquire()
        obj2 = pool.acquire()
        assert pool.available_count() == 0

        pool.release(obj1)
        assert pool.available_count() == 1

        pool.release(obj2)
        assert pool.available_count() == 2

    def test_clear(self):
        """Test clearing the pool."""
        pool = ObjectPool(make_poolable, max_size=5)

        obj = pool.acquire()
        pool.release(obj)

        pool.clear()
        assert pool.available_count() == 0

    def test_repr(self):
        """Test string representation."""
        pool = ObjectPool(make_poolable, max_size=10)
        obj = pool.acquire()
        pool.release(obj)

        repr_str = repr(pool)
        assert "ObjectPool" in repr_str
        assert "max_size=10" in repr_str
        assert "available=1" in repr_str
