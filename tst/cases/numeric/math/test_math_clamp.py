# =============================================================================
# Test: math_clamp
# =============================================================================

"""
Tests for rite.numeric.math.math_clamp.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.math.math_clamp import (
    math_clamp,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value,minimum,maximum,expected",
    [
        (5, 0, 10, 5),  # Value in range
        (-5, 0, 10, 0),  # Value below minimum
        (15, 0, 10, 10),  # Value above maximum
        (0, 0, 10, 0),  # Value equals minimum
        (10, 0, 10, 10),  # Value equals maximum
        (5.5, 0, 10, 5.5),  # Float in range
    ],
)
def test_math_clamp(
    value: float, minimum: float, maximum: float, expected: float
) -> None:
    """Test math_clamp() with various values."""
    assert math_clamp(value, minimum, maximum) == expected
