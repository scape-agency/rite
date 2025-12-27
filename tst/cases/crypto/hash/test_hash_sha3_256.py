# =============================================================================
# Test: hash_sha3_256
# =============================================================================

"""
Tests for rite.crypto.hash.hash_sha3_256.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.hash.hash_sha3_256 import (
    hash_sha3_256,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_hash_sha3_256() -> None:
    """Test hash_sha3_256() function."""
    # Test with string
    result = hash_sha3_256("hello")
    assert len(result) == 64  # sha3-256 produces 32 bytes = 64 hex chars
    
    # Test with bytes
    result2 = hash_sha3_256(b"hello")
    assert result == result2
    
    # Test empty string
    result_empty = hash_sha3_256("")
    assert len(result_empty) == 64
