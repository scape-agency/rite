# =============================================================================
# Test: rounding_round
# =============================================================================

"""
Tests for rite.numeric.rounding.rounding_round.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.rounding.rounding_round import (
    rounding_round,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_rounding_round() -> None:
    """Test rounding_round() function."""
    # Test default (0 decimals)
    assert rounding_round(3.5) == 4.0
    assert rounding_round(2.4) == 2.0

    # Test with decimals
    assert rounding_round(3.14159, 2) == 3.14
    assert rounding_round(3.14159, 4) == 3.1416

    # Test negative
    assert rounding_round(-3.5) == -4.0
