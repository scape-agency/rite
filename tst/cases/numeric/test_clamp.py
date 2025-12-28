# =============================================================================
# Test: clamp
# =============================================================================

"""
Tests for rite.numeric.clamp.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.clamp import (
    clamp,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value, lo, hi, expected",
    [
        (5, 0, 10, 5),
        (-5, 0, 10, 0),
        (15, 0, 10, 10),
        (0, 0, 10, 0),
        (10, 0, 10, 10),
        (None, 0, 10, None),
    ],
)
def test_clamp(
    value: float | None, lo: float, hi: float, expected: float | None
) -> None:
    """Test clamping within, below, and above bounds, including None."""
    assert clamp(value, lo, hi) == expected
