# =============================================================================
# Test: rounding_ceil
# =============================================================================

"""
Tests for rite.numeric.rounding.rounding_ceil.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.numeric.rounding.rounding_ceil import (
    rounding_ceil,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_rounding_ceil() -> None:
    """Test rounding_ceil() function."""
    # Test positive rounding up
    assert rounding_ceil(3.1) == 4
    assert rounding_ceil(3.9) == 4
    
    # Test negative rounding up
    assert rounding_ceil(-3.9) == -3
    assert rounding_ceil(-3.1) == -3
    
    # Test integer
    assert rounding_ceil(4.0) == 4
