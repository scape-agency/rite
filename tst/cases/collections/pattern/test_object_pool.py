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
        # TODO: Implement test
        instance = ObjectPool()
        assert instance is not None

    def test_acquire(self) -> None:
        """Test ObjectPool.acquire() method."""
        # TODO: Implement test
        instance = ObjectPool()
        # result = instance.acquire()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_release(self) -> None:
        """Test ObjectPool.release() method."""
        # TODO: Implement test
        instance = ObjectPool()
        # result = instance.release()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_clear(self) -> None:
        """Test ObjectPool.clear() method."""
        # TODO: Implement test
        instance = ObjectPool()
        # result = instance.clear()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_size(self) -> None:
        """Test ObjectPool.size() method."""
        # TODO: Implement test
        instance = ObjectPool()
        # result = instance.size()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_available_count(self) -> None:
        """Test ObjectPool.available_count() method."""
        # TODO: Implement test
        instance = ObjectPool()
        # result = instance.available_count()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_in_use_count(self) -> None:
        """Test ObjectPool.in_use_count() method."""
        # TODO: Implement test
        instance = ObjectPool()
        # result = instance.in_use_count()
        # assert result is not None
        pytest.skip("Test not implemented")
