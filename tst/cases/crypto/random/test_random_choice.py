# =============================================================================
# Test: random_choice
# =============================================================================

"""
Tests for rite.crypto.random.random_choice.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.random.random_choice import (
    random_choice,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_random_choice() -> None:
    """Test random_choice() function."""
    # Test with list
    choices = ["a", "b", "c", "d", "e"]
    result = random_choice(choices)
    assert result in choices

    # Test with string
    result = random_choice("abcde")
    assert result in "abcde"

    # Test uniqueness (run multiple times)
    results = [random_choice(choices) for _ in range(20)]
    assert len(set(results)) > 1  # Should have variety
