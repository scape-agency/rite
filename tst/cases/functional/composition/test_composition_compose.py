# =============================================================================
# Test: composition_compose
# =============================================================================

"""
Tests for rite.functional.composition.composition_compose.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.functional.composition.composition_compose import (
    composition_compose,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_composition_compose() -> None:
    """Test composition_compose() function."""
    add_one = lambda x: x + 1
    double = lambda x: x * 2

    # compose applies right to left: f(x) = double(add_one(x))
    f = composition_compose(double, add_one)
    # (3 + 1) * 2 = 8
    assert f(3) == 8

    # Test with single function
    g = composition_compose(double)
    assert g(5) == 10
