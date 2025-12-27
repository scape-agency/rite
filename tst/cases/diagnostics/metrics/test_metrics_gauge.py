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

# Import | Standard Library
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
        # TODO: Implement test
        instance = metrics_gauge()
        assert instance is not None

    def test_value(self) -> None:
        """Test metrics_gauge.value() method."""
        # TODO: Implement test
        instance = metrics_gauge()
        # result = instance.value()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_set(self) -> None:
        """Test metrics_gauge.set() method."""
        # TODO: Implement test
        instance = metrics_gauge()
        # result = instance.set()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_increment(self) -> None:
        """Test metrics_gauge.increment() method."""
        # TODO: Implement test
        instance = metrics_gauge()
        # result = instance.increment()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_decrement(self) -> None:
        """Test metrics_gauge.decrement() method."""
        # TODO: Implement test
        instance = metrics_gauge()
        # result = instance.decrement()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_reset(self) -> None:
        """Test metrics_gauge.reset() method."""
        # TODO: Implement test
        instance = metrics_gauge()
        # result = instance.reset()
        # assert result is not None
        pytest.skip("Test not implemented")

