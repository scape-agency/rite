# =============================================================================
# Test: statistics_mean
# =============================================================================

"""
Tests for rite.numeric.statistics.statistics_mean.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.statistics.statistics_mean import (
    statistics_mean,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_statistics_mean() -> None:
    """Test statistics_mean() function for typical inputs."""
    assert statistics_mean([1, 2, 3, 4, 5]) == 3.0
    assert statistics_mean([10, 20, 30]) == 20.0
    assert statistics_mean([5.5]) == 5.5


def test_statistics_mean_empty_raises() -> None:
    """statistics_mean() should raise on empty list."""
    with pytest.raises(ValueError):
        statistics_mean([])
