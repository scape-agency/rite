# =============================================================================
# Test: metrics_counter
# =============================================================================

"""
Tests for rite.diagnostics.metrics.metrics_counter.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.metrics.metrics_counter import (
    metrics_counter,
)

# =============================================================================
# Test Class: metrics_counter
# =============================================================================


class Testmetrics_counter:
    """Tests for metrics_counter class."""

    def test_instantiation(self) -> None:
        """Test metrics_counter can be instantiated."""
        # TODO: Implement test
        instance = metrics_counter()
        assert instance is not None

    def test_value(self) -> None:
        """Test metrics_counter.value() method."""
        # TODO: Implement test
        instance = metrics_counter()
        # result = instance.value()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_increment(self) -> None:
        """Test metrics_counter.increment() method."""
        # TODO: Implement test
        instance = metrics_counter()
        # result = instance.increment()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_reset(self) -> None:
        """Test metrics_counter.reset() method."""
        # TODO: Implement test
        instance = metrics_counter()
        # result = instance.reset()
        # assert result is not None
        pytest.skip("Test not implemented")
