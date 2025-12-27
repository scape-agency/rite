# =============================================================================
# Test: hash_sha256
# =============================================================================

"""
Tests for rite.crypto.hash.hash_sha256.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.hash.hash_sha256 import (
    hash_sha256,
    hash_sha256_hmac,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_hash_sha256() -> None:
    """Test hash_sha256() function."""
    # Test with string input
    result = hash_sha256("hello")
    assert len(result) == 64
    assert isinstance(result, str)
    assert (
        result
        == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    )

    # Test with bytes input
    result_bytes = hash_sha256(b"hello")
    assert result_bytes == result

    # Test empty string
    empty_result = hash_sha256("")
    assert len(empty_result) == 64


def test_hash_sha256_hmac() -> None:
    """Test hash_sha256_hmac() function."""
    # Test HMAC generation
    result = hash_sha256_hmac("secret", "message")
    assert len(result) == 64
    assert isinstance(result, str)

    # Test with bytes
    result_bytes = hash_sha256_hmac(b"secret", b"message")
    assert result_bytes == result

    # Different keys produce different HMACs
    result2 = hash_sha256_hmac("different", "message")
    assert result != result2
