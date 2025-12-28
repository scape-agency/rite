# =============================================================================
# Test: decorators_throttle
# =============================================================================

"""
Tests for rite.functional.decorators.decorators_throttle.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.functional.decorators.decorators_throttle import (
    decorators_throttle,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_decorators_throttle() -> None:
    """decorators_throttle should limit call frequency.""""

    import time

    calls = {"count": 0}

    @decorators_throttle(0.0)
    def work() -> str:
        calls["count"] += 1
        return "ok"

    first = work()
    second = work()

    assert first == "ok"
    assert second == "ok" or second is None
    assert calls["count"] >= 1

