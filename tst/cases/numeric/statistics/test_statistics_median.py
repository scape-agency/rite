# =============================================================================
# Test: statistics_median
# =============================================================================

"""
Tests for rite.numeric.statistics.statistics_median.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.statistics.statistics_median import (
    statistics_median,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_statistics_median() -> None:
    """Test statistics_median() for odd and even length lists."""
    assert statistics_median([1, 2, 3, 4, 5]) == 3
    assert statistics_median([1, 2, 3, 4]) == 2.5
    assert statistics_median([5]) == 5


def test_statistics_median_empty_raises() -> None:
    """statistics_median() should raise on empty list."""
    with pytest.raises(ValueError):
        statistics_median([])
