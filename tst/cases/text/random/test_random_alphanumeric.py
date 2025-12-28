# =============================================================================
# Test: random_alphanumeric
# =============================================================================

"""
Tests for rite.text.random.random_alphanumeric.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import string

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.random.random_alphanumeric import (
    random_alphanumeric,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_random_alphanumeric() -> None:
    """Test random_alphanumeric() function."""
    result = random_alphanumeric(10)
    assert isinstance(result, str)
    assert len(result) == 10


def test_random_alphanumeric_default_length() -> None:
    """Test random_alphanumeric with default length."""
    result = random_alphanumeric()
    assert len(result) == 16


def test_random_alphanumeric_lowercase_only() -> None:
    """Test random_alphanumeric with lowercase only."""
    result = random_alphanumeric(
        20, include_lowercase=True, include_uppercase=False
    )
    assert all(c in string.ascii_lowercase + string.digits for c in result)
    # At least some should be lowercase (not all digits)
    assert any(c in string.ascii_lowercase for c in result) or len(result) == 0


def test_random_alphanumeric_uppercase_only() -> None:
    """Test random_alphanumeric with uppercase only."""
    result = random_alphanumeric(
        20, include_lowercase=False, include_uppercase=True
    )
    assert all(c in string.ascii_uppercase + string.digits for c in result)


def test_random_alphanumeric_both_cases() -> None:
    """Test random_alphanumeric with both cases."""
    result = random_alphanumeric(50)
    assert all(c in string.ascii_letters + string.digits for c in result)


def test_random_alphanumeric_no_letters_raises() -> None:
    """Test random_alphanumeric raises when no letters are included."""
    with pytest.raises(ValueError, match="At least one"):
        random_alphanumeric(
            10, include_lowercase=False, include_uppercase=False
        )


def test_random_alphanumeric_uniqueness() -> None:
    """Test that random_alphanumeric produces different results."""
    results = {random_alphanumeric(20) for _ in range(10)}
    # With 62^20 combinations, collisions are virtually impossible
    assert len(results) == 10
