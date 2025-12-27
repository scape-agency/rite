# =============================================================================
# Test: math_pow
# =============================================================================

"""
Tests for rite.numeric.math.math_pow.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.math.math_pow import (
    math_pow,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "base,exponent,expected",
    [
        (2, 3, 8.0),  # 2^3 = 8
        (5, 2, 25.0),  # 5^2 = 25
        (10, 0, 1.0),  # 10^0 = 1
        (2, -1, 0.5),  # 2^-1 = 0.5
        (3, 3, 27.0),  # 3^3 = 27
        (1.5, 2, 2.25),  # 1.5^2 = 2.25
    ],
)
def test_math_pow(base: float, exponent: float, expected: float) -> None:
    """Test math_pow() with various bases and exponents."""
    assert math_pow(base, exponent) == expected
