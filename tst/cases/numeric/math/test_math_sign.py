# =============================================================================
# Test: math_sign
# =============================================================================

"""
Tests for rite.numeric.math.math_sign.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.math.math_sign import (
    math_sign,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value,expected",
    [
        (5, 1),       # Positive
        (-5, -1),     # Negative
        (0, 0),       # Zero
        (3.14, 1),    # Positive float
        (-3.14, -1),  # Negative float
    ],
)
def test_math_sign(value: float, expected: int) -> None:
    """Test math_sign() with various values."""
    assert math_sign(value) == expected
