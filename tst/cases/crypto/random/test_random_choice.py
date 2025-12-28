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


def test_random_choice_edge_cases() -> None:
    """Test random_choice() edge cases."""
    # Test with single element list
    result = random_choice([42])
    assert result == 42

    # Test with single character string
    result = random_choice("X")
    assert result == "X"

    # Test with tuple
    result = random_choice((1, 2, 3))
    assert result in (1, 2, 3)

    # Test with range
    result = random_choice(range(5))
    assert result in range(5)


def test_random_choice_empty_sequence() -> None:
    """Test random_choice() raises IndexError for empty sequence."""
    with pytest.raises(IndexError):
        random_choice([])
    with pytest.raises(IndexError):
        random_choice("")
    with pytest.raises(IndexError):
        random_choice(())
