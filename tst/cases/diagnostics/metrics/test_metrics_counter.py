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
        instance = metrics_counter("test_counter")
        assert instance is not None
        assert instance.name == "test_counter"
        assert instance.value == 0.0

    def test_value(self) -> None:
        """Test metrics_counter.value property."""
        instance = metrics_counter("test_counter")
        assert instance.value == 0.0
        instance.increment()
        assert instance.value == 1.0

    def test_increment(self) -> None:
        """Test metrics_counter.increment() method."""
        instance = metrics_counter("test_counter")
        instance.increment()
        assert instance.value == 1.0
        instance.increment(5)
        assert instance.value == 6.0

    def test_reset(self) -> None:
        """Test metrics_counter.reset() method."""
        instance = metrics_counter("test_counter")
        instance.increment(10)
        instance.reset()
        assert instance.value == 0.0
