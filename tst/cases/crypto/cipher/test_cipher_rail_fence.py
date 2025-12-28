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


def test_encode_rail_fence_edge_case_rails_too_few() -> None:
    """Test with num_rails < 2 (line 46)."""
    result = encode_rail_fence_cipher("HELLO", 1)
    assert result == "HELLO"


def test_decode_rail_fence_edge_case_rails_too_few() -> None:
    """Test decoding with num_rails < 2 (line 79)."""
    result = decode_rail_fence_cipher("HELLO", 1)
    assert result == "HELLO"


def test_encode_rail_fence_edge_case_rails_too_many() -> None:
    """Test with num_rails >= len(text)."""
    result = encode_rail_fence_cipher("HI", 5)
    assert result == "HI"


def test_rail_fence_longer_text() -> None:
    """Test with longer text."""
    text = "THE QUICK BROWN FOX"
    encoded = encode_rail_fence_cipher(text, 4)
    decoded = decode_rail_fence_cipher(encoded, 4)
    assert decoded == text
