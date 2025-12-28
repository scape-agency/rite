# =============================================================================
# Test: metrics_histogram
# =============================================================================

"""
Tests for rite.diagnostics.metrics.metrics_histogram.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.diagnostics.metrics.metrics_histogram import (
    metrics_histogram,
)

# =============================================================================
# Test Class: metrics_histogram
# =============================================================================


class Testmetrics_histogram:
    """Tests for metrics_histogram class."""

    def test_instantiation(self) -> None:
        """Test metrics_histogram can be instantiated."""
        instance = metrics_histogram("test_histogram")
        assert instance is not None
        assert instance.name == "test_histogram"
        assert instance.count == 0

    def test_count(self) -> None:
        """Test metrics_histogram.count property."""
        instance = metrics_histogram("test_histogram")
        assert instance.count == 0
        instance.observe(10.0)
        assert instance.count == 1

    def test_sum(self) -> None:
        """Test metrics_histogram.sum property."""
        instance = metrics_histogram("test_histogram")
        instance.observe(10.0)
        instance.observe(20.0)
        assert instance.sum == 30.0

    def test_mean(self) -> None:
        """Test metrics_histogram.mean property."""
        instance = metrics_histogram("test_histogram")
        instance.observe(10.0)
        instance.observe(20.0)
        instance.observe(30.0)
        assert instance.mean == 20.0

    def test_median(self) -> None:
        """Test metrics_histogram.median property."""
        instance = metrics_histogram("test_histogram")
        instance.observe(10.0)
        instance.observe(20.0)
        instance.observe(30.0)
        assert instance.median == 20.0

    def test_observe(self) -> None:
        """Test metrics_histogram.observe() method."""
        instance = metrics_histogram("test_histogram")
        instance.observe(42.5)
        assert instance.count == 1
        assert 42.5 in instance._values

    def test_percentile(self) -> None:
        """Test metrics_histogram.percentile() method."""
        instance = metrics_histogram("test_histogram")
        for i in range(1, 101):
            instance.observe(float(i))
        assert instance.percentile(50) == 50.5
        assert instance.percentile(95) == 95.95

    def test_reset(self) -> None:
        """Test metrics_histogram.reset() method."""
        instance = metrics_histogram("test_histogram")
        instance.observe(10.0)
        instance.observe(20.0)
        instance.reset()
        assert instance.count == 0
        assert instance.sum == 0.0

    def test_mean_empty(self) -> None:
        """Test metrics_histogram.mean on empty histogram."""
        instance = metrics_histogram("test_histogram")
        assert instance.mean == 0.0

    def test_median_empty(self) -> None:
        """Test metrics_histogram.median on empty histogram."""
        instance = metrics_histogram("test_histogram")
        assert instance.median == 0.0

    def test_percentile_empty(self) -> None:
        """Test metrics_histogram.percentile on empty histogram."""
        instance = metrics_histogram("test_histogram")
        assert instance.percentile(50) == 0.0

    def test_percentile_single_value(self) -> None:
        """Test metrics_histogram.percentile with single value."""
        instance = metrics_histogram("test_histogram")
        instance.observe(42.0)
        result = instance.percentile(50)
        assert result == 42.0

    def test_repr(self) -> None:
        """Test metrics_histogram __repr__ method."""
        instance = metrics_histogram("test_histogram")
        instance.observe(10.0)
        result = repr(instance)
        assert "test_histogram" in result
