# =============================================================================
# Test: partial_apply
# =============================================================================

"""
Tests for rite.functional.partial.partial_apply.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.functional.partial.partial_apply import (
    partial_apply,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_partial_apply() -> None:
    """partial_apply should fix positional and keyword arguments.""""

    def multiply(x: int, y: int, z: int) -> int:
        return x * y * z

    double = partial_apply(multiply, 2)
    assert double(3, 4) == 24

    def power(base: int, exponent: int) -> int:
        return base**exponent

    square = partial_apply(power, exponent=2)
    assert square(5) == 25

