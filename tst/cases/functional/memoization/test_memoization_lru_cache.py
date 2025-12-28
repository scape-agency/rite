# =============================================================================
# Test: memoization_lru_cache
# =============================================================================

"""
Tests for rite.functional.memoization.memoization_lru_cache.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.functional.memoization.memoization_lru_cache import (
    memoization_lru_cache,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_memoization_lru_cache() -> None:
    """memoization_lru_cache should apply functools.lru_cache behavior.""""

    calls = {"count": 0}

    @memoization_lru_cache(maxsize=2)
    def square(x: int) -> int:
        calls["count"] += 1
        return x * x

    assert square(2) == 4
    assert square(2) == 4
    assert calls["count"] == 1

    assert square(3) == 9
    assert calls["count"] == 2

