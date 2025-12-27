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

# Import | Libraries
import pytest

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
