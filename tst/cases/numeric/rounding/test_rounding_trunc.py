# =============================================================================
# Test: rounding_trunc
# =============================================================================

"""
Tests for rite.numeric.rounding.rounding_trunc.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.rounding.rounding_trunc import (
    rounding_trunc,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_rounding_trunc() -> None:
    """Test rounding_trunc() function."""
    # Test positive truncation
    assert rounding_trunc(3.9) == 3
    assert rounding_trunc(3.1) == 3
    
    # Test negative truncation (towards zero)
    assert rounding_trunc(-3.9) == -3
    assert rounding_trunc(-3.1) == -3
    
    # Test integer
    assert rounding_trunc(4.0) == 4
