# =============================================================================
# Test: hash_md5
# =============================================================================

"""
Tests for rite.crypto.hash.hash_md5.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.hash.hash_md5 import (
    hash_md5,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_hash_md5() -> None:
    """Test hash_md5() function."""
    # Test with string
    assert hash_md5("hello") == "5d41402abc4b2a76b9719d911017c592"
    
    # Test with bytes
    assert hash_md5(b"hello") == "5d41402abc4b2a76b9719d911017c592"
    
    # Test empty string
    assert hash_md5("") == "d41d8cd98f00b204e9800998ecf8427e"
    
    # Test different encoding
    assert hash_md5("hello", encoding="utf-8") == "5d41402abc4b2a76b9719d911017c592"
