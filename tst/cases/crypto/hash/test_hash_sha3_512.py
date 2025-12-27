# =============================================================================
# Test: hash_sha3_512
# =============================================================================

"""
Tests for rite.crypto.hash.hash_sha3_512.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.hash.hash_sha3_512 import (
    hash_sha3_512,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_hash_sha3_512() -> None:
    """Test hash_sha3_512() function."""
    # Test with string
    result = hash_sha3_512("hello")
    assert len(result) == 128  # sha3-512 produces 64 bytes = 128 hex chars
    
    # Test with bytes
    result2 = hash_sha3_512(b"hello")
    assert result == result2
    
    # Test empty string
    result_empty = hash_sha3_512("")
    assert len(result_empty) == 128
