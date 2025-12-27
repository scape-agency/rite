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

# Import | Standard Library
import pytest

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
        # TODO: Implement test
        instance = metrics_timer()
        assert instance is not None

    def test_count(self) -> None:
        """Test metrics_timer.count() method."""
        # TODO: Implement test
        instance = metrics_timer()
        # result = instance.count()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_total(self) -> None:
        """Test metrics_timer.total() method."""
        # TODO: Implement test
        instance = metrics_timer()
        # result = instance.total()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_average(self) -> None:
        """Test metrics_timer.average() method."""
        # TODO: Implement test
        instance = metrics_timer()
        # result = instance.average()
        # assert result is not None
        pytest.skip("Test not implemented")

    def test_reset(self) -> None:
        """Test metrics_timer.reset() method."""
        # TODO: Implement test
        instance = metrics_timer()
        # result = instance.reset()
        # assert result is not None
        pytest.skip("Test not implemented")

