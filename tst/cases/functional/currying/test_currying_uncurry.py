# =============================================================================
# Test: currying_uncurry
# =============================================================================

"""
Tests for rite.functional.currying.currying_uncurry.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.functional.currying.currying_uncurry import (
    currying_uncurry,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_currying_uncurry() -> None:
    """Test that currying_uncurry restores multi-arg calling convention."""

    def make_curried() -> callable:
        return lambda a: lambda b: lambda c: a + b + c

    curried = make_curried()
    uncurried = currying_uncurry(curried, 3)

    assert uncurried(1, 2, 3) == 6

    with pytest.raises(TypeError):
        uncurried(1, 2)
