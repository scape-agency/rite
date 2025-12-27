# =============================================================================
# Test: math_abs
# =============================================================================

"""
Tests for rite.numeric.math.math_abs.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.math.math_abs import (
    math_abs,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "value,expected",
    [
        (5, 5),  # Positive
        (-5, 5),  # Negative
        (0, 0),  # Zero
        (3.14, 3.14),  # Positive float
        (-3.14, 3.14),  # Negative float
    ],
)
def test_math_abs(value: float, expected: float) -> None:
    """Test math_abs() with various values."""
    assert math_abs(value) == expected
