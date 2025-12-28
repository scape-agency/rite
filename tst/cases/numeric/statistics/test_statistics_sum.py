# =============================================================================
# Test: statistics_sum
# =============================================================================

"""
Tests for rite.numeric.statistics.statistics_sum.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.statistics.statistics_sum import (
    statistics_sum,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_statistics_sum() -> None:
    """Test statistics_sum() for various input lists."""
    assert statistics_sum([1, 2, 3, 4, 5]) == 15
    assert statistics_sum([10, 20, 30]) == 60
    assert statistics_sum([]) == 0
