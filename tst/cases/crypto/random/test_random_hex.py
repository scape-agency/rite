# =============================================================================
# Test: random_hex
# =============================================================================

"""
Tests for rite.crypto.random.random_hex.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.random.random_hex import (
    random_hex,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_random_hex() -> None:
    """Test random_hex() function."""
    # Test default size
    result = random_hex()
    assert isinstance(result, str)
    assert len(result) == 64  # 32 bytes = 64 hex chars
    assert all(c in "0123456789abcdef" for c in result)

    # Test custom size
    result = random_hex(16)
    assert len(result) == 32  # 16 bytes = 32 hex chars

    # Test uniqueness
    result1 = random_hex(16)
    result2 = random_hex(16)
    assert result1 != result2


def test_random_hex_edge_cases() -> None:
    """Test random_hex() edge cases."""
    # Test zero bytes
    result = random_hex(0)
    assert isinstance(result, str)
    assert len(result) == 0

    # Test single byte
    result = random_hex(1)
    assert isinstance(result, str)
    assert len(result) == 2  # 1 byte = 2 hex chars
    assert all(c in "0123456789abcdef" for c in result)

    # Test large size
    result = random_hex(512)
    assert isinstance(result, str)
    assert len(result) == 1024  # 512 bytes = 1024 hex chars
