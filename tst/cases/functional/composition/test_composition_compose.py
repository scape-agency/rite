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


def test_composition_compose_empty() -> None:
    """Test composition_compose with no functions (line 68)."""
    f = composition_compose()
    # Should return identity function
    assert f(5) == 5
    assert f("hello") == "hello"


def test_composition_compose_multiple() -> None:
    """Test composition_compose with multiple functions."""
    add_one = lambda x: x + 1
    double = lambda x: x * 2
    square = lambda x: x**2

    # compose applies right to left
    f = composition_compose(add_one, double, square)
    # square(2) = 4, double(4) = 8, add_one(8) = 9
    assert f(2) == 9
