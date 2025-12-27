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

# Import | Standard Library
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
        """Test SingletonMeta can be instantiated."""
        # TODO: Implement test
        instance = SingletonMeta()
        assert instance is not None

    def test_reset_instance(self) -> None:
        """Test SingletonMeta.reset_instance() method."""
        # TODO: Implement test
        instance = SingletonMeta()
        # result = instance.reset_instance()
        # assert result is not None
        pytest.skip("Test not implemented")

