# =============================================================================
# Test: statistics_min_max
# =============================================================================

"""
Tests for rite.numeric.statistics.statistics_min_max.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.statistics.statistics_min_max import (
    statistics_max,
    statistics_min,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_statistics_min() -> None:
    """Test statistics_min() returns minimum value and errors on empty."""
    assert statistics_min([3, 1, 4, 1, 5]) == 1
    assert statistics_min([10, 20, 5]) == 5

    with pytest.raises(ValueError):
        statistics_min([])


def test_statistics_max() -> None:
    """Test statistics_max() returns maximum value and errors on empty."""
    assert statistics_max([3, 1, 4, 1, 5]) == 5
    assert statistics_max([10, 20, 5]) == 20

    with pytest.raises(ValueError):
        statistics_max([])
