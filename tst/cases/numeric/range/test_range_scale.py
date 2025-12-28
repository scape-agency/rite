# =============================================================================
# Test: range_scale
# =============================================================================

"""
Tests for rite.numeric.range.range_scale.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.range.range_scale import (
    range_scale,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value, from_min, from_max, to_min, to_max, expected",
    [
        (5, 0, 10, 0, 100, 50.0),
        (0, 0, 10, 100, 200, 100.0),
        (10, 0, 10, 100, 200, 200.0),
        (5, 5, 5, 0, 100, 0.0),  # degenerate from range
    ],
)
def test_range_scale(
    value: float,
    from_min: float,
    from_max: float,
    to_min: float,
    to_max: float,
    expected: float,
) -> None:
    """Test scaling between ranges including degenerate source range."""
    assert range_scale(value, from_min, from_max, to_min, to_max) == expected
