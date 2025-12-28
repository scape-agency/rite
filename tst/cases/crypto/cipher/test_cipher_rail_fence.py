# =============================================================================
# Test: cipher_rail_fence
# =============================================================================

"""
Tests for rite.crypto.cipher.cipher_rail_fence.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.cipher.cipher_rail_fence import (
    decode_rail_fence_cipher,
    encode_rail_fence_cipher,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_encode_rail_fence_cipher() -> None:
    """Test encode_rail_fence_cipher() function."""
    result = encode_rail_fence_cipher("HELLO", 3)
    assert isinstance(result, str)
    assert len(result) == len("HELLO")


def test_decode_rail_fence_cipher() -> None:
    """Test decode_rail_fence_cipher() function."""
    encoded = encode_rail_fence_cipher("HELLO", 3)
    result = decode_rail_fence_cipher(encoded, 3)
    assert result == "HELLO"
    assert isinstance(result, str)
