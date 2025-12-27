# =============================================================================
# Test: hash_blake2b
# =============================================================================

"""
Tests for rite.crypto.hash.hash_blake2b.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.hash.hash_blake2b import (
    hash_blake2b,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_hash_blake2b() -> None:
    """Test hash_blake2b() function."""
    # Test with string
    result = hash_blake2b("hello")
    assert len(result) == 128  # blake2b produces 64 bytes = 128 hex chars
    
    # Test with bytes
    result2 = hash_blake2b(b"hello")
    assert result == result2
    
    # Test empty string
    result_empty = hash_blake2b("")
    assert len(result_empty) == 128
