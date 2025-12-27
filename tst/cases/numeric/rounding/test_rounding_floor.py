# =============================================================================
# Test: rounding_floor
# =============================================================================

"""
Tests for rite.numeric.rounding.rounding_floor.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.rounding.rounding_floor import (
    rounding_floor,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_rounding_floor() -> None:
    """Test rounding_floor() function."""
    # Test positive rounding down
    assert rounding_floor(3.1) == 3
    assert rounding_floor(3.9) == 3
    
    # Test negative rounding down
    assert rounding_floor(-3.1) == -4
    assert rounding_floor(-3.9) == -4
    
    # Test integer
    assert rounding_floor(4.0) == 4
