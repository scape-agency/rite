# =============================================================================
# Test: metrics_timer
# =============================================================================

"""
Tests for rite.diagnostics.metrics.metrics_timer.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.diagnostics.metrics.metrics_timer import (
    metrics_timer,
)

# =============================================================================
# Test Class: metrics_timer
# =============================================================================


class Testmetrics_timer:
    """Tests for metrics_timer class."""

    def test_instantiation(self) -> None:
        """Test metrics_timer can be instantiated."""
        instance = metrics_timer("test_timer")
        assert instance is not None
        assert instance.name == "test_timer"
        assert instance.count == 0

    def test_count(self) -> None:
        """Test metrics_timer.count property."""
        instance = metrics_timer("test_timer")
        assert instance.count == 0
        with instance:
            pass
        assert instance.count == 1

    def test_total(self) -> None:
        """Test metrics_timer.total property."""
        instance = metrics_timer("test_timer")
        with instance:
            pass
        assert instance.total > 0.0

    def test_average(self) -> None:
        """Test metrics_timer.average property."""
        instance = metrics_timer("test_timer")
        with instance:
            pass
        assert instance.average > 0.0
        assert instance.average == instance.total / instance.count

    def test_average_zero_count(self) -> None:
        """Test metrics_timer.average returns 0 when no measurements."""
        instance = metrics_timer("test_timer")
        assert instance.count == 0
        assert instance.average == 0.0

    def test_reset(self) -> None:
        """Test metrics_timer.reset() method."""
        instance = metrics_timer("test_timer")
        with instance:
            pass
        instance.reset()
        assert instance.count == 0
        assert instance.total == 0.0
