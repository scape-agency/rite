# =============================================================================
# Test: memoization_memoize
# =============================================================================

"""
Tests for rite.functional.memoization.memoization_memoize.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.functional.memoization.memoization_memoize import (
    memoization_memoize,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_memoization_memoize() -> None:
    """memoization_memoize should cache results based on arguments.""""

    calls: dict[str, int] = {"count": 0}

    @memoization_memoize()
    def inc(x: int) -> int:
        calls["count"] += 1
        return x + 1

    assert inc(1) == 2
    assert inc(1) == 2
    assert calls["count"] == 1

    assert inc(2) == 3
    assert calls["count"] == 2

