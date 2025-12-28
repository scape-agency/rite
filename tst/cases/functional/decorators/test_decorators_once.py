# =============================================================================
# Test: decorators_once
# =============================================================================

"""
Tests for rite.functional.decorators.decorators_once.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.functional.decorators.decorators_once import (
    decorators_once,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_decorators_once() -> None:
    """decorators_once should only execute the function once."""

    calls = {"count": 0}

    @decorators_once()
    def get_value() -> int:
        calls["count"] += 1
        return 42

    assert get_value() == 42
    assert get_value() == 42
    assert calls["count"] == 1
