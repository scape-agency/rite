# =============================================================================
# Test: value_to_decimal
# =============================================================================

"""
Tests for rite.numeric.value_to_decimal.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.numeric.value_to_decimal import (
    value_to_decimal,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_value_to_decimal_valid_inputs() -> None:
    """Test value_to_decimal() with valid convertible inputs.""""
    from decimal import Decimal

    assert value_to_decimal(12.5) == Decimal("12.5")
    assert value_to_decimal("12.5") == Decimal("12.5")

    dec = Decimal("3.14")
    assert value_to_decimal(dec) is dec


def test_value_to_decimal_invalid_inputs() -> None:
    """Test value_to_decimal() with invalid and None inputs.""""
    with pytest.raises(ValueError):
        value_to_decimal(None)

    with pytest.raises(ValueError):
        value_to_decimal("not-a-number")

