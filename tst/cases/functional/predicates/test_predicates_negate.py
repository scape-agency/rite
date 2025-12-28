# =============================================================================
# Test: predicates_negate
# =============================================================================

"""
Tests for rite.functional.predicates.predicates_negate.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.functional.predicates.predicates_negate import (
    predicates_negate,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_predicates_negate_inverts_predicate() -> None:
    """predicates_negate() returns a predicate with inverted result.""""
    is_even = lambda x: x % 2 == 0
    is_odd = predicates_negate(is_even)

    assert is_even(2) is True
    assert is_even(3) is False

    assert is_odd(2) is False
    assert is_odd(3) is True

