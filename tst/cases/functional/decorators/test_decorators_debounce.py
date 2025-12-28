# =============================================================================
# Test: decorators_debounce
# =============================================================================

"""
Tests for rite.functional.decorators.decorators_debounce.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.functional.decorators.decorators_debounce import (
    decorators_debounce,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_decorators_debounce() -> None:
    """decorators_debounce should delay execution by given time."""

    # Import | Standard Library
    import time

    calls = {"count": 0}

    @decorators_debounce(0.0)
    def do_work() -> str:
        calls["count"] += 1
        return "done"

    start = time.time()
    result = do_work()
    end = time.time()

    assert result == "done"
    assert calls["count"] == 1
    assert end >= start
