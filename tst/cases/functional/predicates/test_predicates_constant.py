# =============================================================================
# Test: predicates_constant
# =============================================================================

"""
Tests for rite.functional.predicates.predicates_constant.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.functional.predicates.predicates_constant import (
    predicates_constant,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_predicates_constant_returns_same_value() -> None:
    """Function returned by predicates_constant() always yields same value."""
    const_true = predicates_constant(True)
    const_42 = predicates_constant(42)

    assert const_true() is True
    assert const_true(1, 2, key="value") is True

    assert const_42("anything") == 42
