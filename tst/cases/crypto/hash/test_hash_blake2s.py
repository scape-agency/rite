# =============================================================================
# Test: hash_blake2s
# =============================================================================

"""
Tests for rite.crypto.hash.hash_blake2s.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.hash.hash_blake2s import (
    hash_blake2s,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_hash_blake2s() -> None:
    """Test hash_blake2s() function."""
    # Test with string
    result = hash_blake2s("hello")
    assert len(result) == 64  # blake2s produces 32 bytes = 64 hex chars
    
    # Test with bytes
    result2 = hash_blake2s(b"hello")
    assert result == result2
    
    # Test empty string
    result_empty = hash_blake2s("")
    assert len(result_empty) == 64
