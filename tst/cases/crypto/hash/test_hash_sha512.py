# =============================================================================
# Test: hash_sha512
# =============================================================================

"""
Tests for rite.crypto.hash.hash_sha512.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.crypto.hash.hash_sha512 import (
    hash_sha512,
    hash_sha512_hmac,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_hash_sha512() -> None:
    """Test hash_sha512() function."""
    # Test with string input
    result = hash_sha512("hello")
    assert len(result) == 128
    assert isinstance(result, str)
    assert (
        result
        == "9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca7"
        "2323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043"
    )

    # Test with bytes input
    result_bytes = hash_sha512(b"hello")
    assert result_bytes == result

    # Test empty string
    empty_result = hash_sha512("")
    assert len(empty_result) == 128

    # Test different inputs produce different hashes
    result2 = hash_sha512("world")
    assert result != result2


def test_hash_sha512_hmac() -> None:
    """Test hash_sha512_hmac() function."""
    # Test HMAC generation
    result = hash_sha512_hmac("secret", "message")
    assert len(result) == 128
    assert isinstance(result, str)

    # Test with bytes
    result_bytes = hash_sha512_hmac(b"secret", b"message")
    assert result_bytes == result

    # Different keys produce different HMACs
    result2 = hash_sha512_hmac("different", "message")
    assert result != result2

    # Same key and message produce same HMAC (deterministic)
    result3 = hash_sha512_hmac("secret", "message")
    assert result == result3
