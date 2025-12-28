# =============================================================================
# Test: random_bytes
# =============================================================================

"""
Tests for rite.crypto.random.random_bytes.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.random.random_bytes import (
    random_bytes,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_random_bytes() -> None:
    """Test random_bytes() function."""
    # Test default size
    result = random_bytes()
    assert isinstance(result, bytes)
    assert len(result) == 32  # Default size

    # Test custom size
    result = random_bytes(16)
    assert isinstance(result, bytes)
    assert len(result) == 16

    # Test uniqueness
    result1 = random_bytes(16)
    result2 = random_bytes(16)
    assert result1 != result2  # Should be different


def test_random_bytes_edge_cases() -> None:
    """Test random_bytes() edge cases."""
    # Test zero bytes
    result = random_bytes(0)
    assert isinstance(result, bytes)
    assert len(result) == 0

    # Test single byte
    result = random_bytes(1)
    assert isinstance(result, bytes)
    assert len(result) == 1

    # Test large size
    result = random_bytes(1024)
    assert isinstance(result, bytes)
    assert len(result) == 1024
