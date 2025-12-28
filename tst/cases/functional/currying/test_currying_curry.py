# =============================================================================
# Test: currying_curry
# =============================================================================

"""
Tests for rite.functional.currying.currying_curry.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.functional.currying.currying_curry import (
    currying_curry,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_currying_curry() -> None:
    """Test that currying_curry transforms function into curried form."""

    def add(a: int, b: int, c: int) -> int:
        return a + b + c

    curried = currying_curry(add)

    assert curried(1)(2)(3) == 6  # type: ignore[operator]

    partial_ab = curried(1, 2)
    assert partial_ab(3) == 6  # type: ignore[operator]

    assert curried(1, 2, 3, 99) == 6
