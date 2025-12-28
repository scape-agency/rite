# =============================================================================
# Test: predicates_identity
# =============================================================================

"""
Tests for rite.functional.predicates.predicates_identity.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.functional.predicates.predicates_identity import (
    predicates_identity,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_predicates_identity_returns_input() -> None:
    """predicates_identity() returns the input unchanged."""
    assert predicates_identity(42) == 42
    assert predicates_identity("hello") == "hello"

    data = [1, 2, 3]
    assert predicates_identity(data) is data
