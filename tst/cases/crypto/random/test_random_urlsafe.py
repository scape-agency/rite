# =============================================================================
# Test: random_urlsafe
# =============================================================================

"""
Tests for rite.crypto.random.random_urlsafe.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.crypto.random.random_urlsafe import (
    random_urlsafe,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_random_urlsafe() -> None:
    """Test random_urlsafe() function."""
    # Test default size
    result = random_urlsafe()
    assert isinstance(result, str)
    # URL-safe base64 uses A-Za-z0-9_-
    assert all(c.isalnum() or c in "-_" for c in result)

    # Test custom size
    result = random_urlsafe(32)
    assert isinstance(result, str)

    # Test uniqueness
    result1 = random_urlsafe(16)
    result2 = random_urlsafe(16)
    assert result1 != result2


def test_random_urlsafe_edge_cases() -> None:
    """Test random_urlsafe() edge cases."""
    # Test zero bytes
    result = random_urlsafe(0)
    assert isinstance(result, str)
    assert len(result) == 0

    # Test single byte
    result = random_urlsafe(1)
    assert isinstance(result, str)
    assert len(result) >= 1
    assert all(c.isalnum() or c in "-_" for c in result)

    # Test large size
    result = random_urlsafe(256)
    assert isinstance(result, str)
    assert all(c.isalnum() or c in "-_" for c in result)
