# =============================================================================
# Test: metrics_gauge
# =============================================================================

"""
Tests for rite.diagnostics.metrics.metrics_gauge.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.diagnostics.metrics.metrics_gauge import (
    metrics_gauge,
)

# =============================================================================
# Test Class: metrics_gauge
# =============================================================================


class Testmetrics_gauge:
    """Tests for metrics_gauge class."""

    def test_instantiation(self) -> None:
        """Test metrics_gauge can be instantiated."""
        instance = metrics_gauge("test_gauge")
        assert instance is not None
        assert instance.name == "test_gauge"
        assert instance.value == 0.0

    def test_value(self) -> None:
        """Test metrics_gauge.value property."""
        instance = metrics_gauge("test_gauge")
        assert instance.value == 0.0
        instance.set(42.5)
        assert instance.value == 42.5

    def test_set(self) -> None:
        """Test metrics_gauge.set() method."""
        instance = metrics_gauge("test_gauge")
        instance.set(10.0)
        assert instance.value == 10.0

    def test_increment(self) -> None:
        """Test metrics_gauge.increment() method."""
        instance = metrics_gauge("test_gauge")
        instance.increment(5.0)
        assert instance.value == 5.0
        instance.increment()
        assert instance.value == 6.0

    def test_decrement(self) -> None:
        """Test metrics_gauge.decrement() method."""
        instance = metrics_gauge("test_gauge")
        instance.set(10.0)
        instance.decrement(3.0)
        assert instance.value == 7.0
        instance.decrement()
        assert instance.value == 6.0

    def test_reset(self) -> None:
        """Test metrics_gauge.reset() method."""
        instance = metrics_gauge("test_gauge")
        instance.set(100.0)
        instance.reset()
        assert instance.value == 0.0
