# =============================================================================
# Test: singleton
# =============================================================================

"""
Tests for rite.collections.pattern.singleton.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.pattern.singleton import (
    SingletonMeta,
)

# =============================================================================
# Test Class: SingletonMeta
# =============================================================================


class TestSingletonMeta:
    """Tests for SingletonMeta class."""

    def test_instantiation(self) -> None:
        """Test SingletonMeta can be used as a metaclass."""

        class TestSingleton(metaclass=SingletonMeta):
            """Test singleton class."""

            def __init__(self, value: str = "default") -> None:
                self.value = value

        instance1 = TestSingleton("first")
        instance2 = TestSingleton("second")

        # Both should be the same instance
        assert instance1 is instance2
        # Value should be updated to second
        assert instance1.value == "second"

        # Clean up
        SingletonMeta.reset_instance(TestSingleton)

    def test_reset_instance(self) -> None:
        """Test SingletonMeta.reset_instance() method."""

        class TestSingleton(metaclass=SingletonMeta):
            """Test singleton class."""

            def __init__(self, value: str = "default") -> None:
                self.value = value

        instance1 = TestSingleton("first")
        SingletonMeta.reset_instance(TestSingleton)
        instance2 = TestSingleton("second")

        # After reset, they should be different instances
        assert instance1 is not instance2
        assert instance1.value == "first"
        assert instance2.value == "second"

        # Clean up
        SingletonMeta.reset_instance(TestSingleton)
