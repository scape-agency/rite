# =============================================================================
# Test: composition_pipe
# =============================================================================

"""
Tests for rite.functional.composition.composition_pipe.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.functional.composition.composition_pipe import (
    composition_pipe,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_composition_pipe() -> None:
    """Test composition_pipe() function."""
    add_one = lambda x: x + 1
    double = lambda x: x * 2

    # pipe applies left to right: f(x) = double(add_one(x))
    f = composition_pipe(add_one, double)
    # (3 + 1) * 2 = 8
    assert f(3) == 8

    # Test with single function
    g = composition_pipe(double)
    assert g(5) == 10


def test_composition_pipe_empty() -> None:
    """Test composition_pipe with no functions (line 62)."""
    f = composition_pipe()
    # Should return identity function
    assert f(5) == 5
    assert f("hello") == "hello"


def test_composition_pipe_multiple() -> None:
    """Test composition_pipe with multiple functions."""
    add_one = lambda x: x + 1
    double = lambda x: x * 2
    square = lambda x: x**2

    # pipe applies left to right
    f = composition_pipe(add_one, double, square)
    # add_one(2) = 3, double(3) = 6, square(6) = 36
    assert f(2) == 36
