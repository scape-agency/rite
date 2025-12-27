# =============================================================================
# Test: hash_sha1
# =============================================================================

"""
Tests for rite.crypto.hash.hash_sha1.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.hash.hash_sha1 import (
    hash_sha1,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_hash_sha1() -> None:
    """Test hash_sha1() function."""
    # Test with string
    assert hash_sha1("hello") == "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"

    # Test with bytes
    assert hash_sha1(b"hello") == "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d"

    # Test empty string
    assert hash_sha1("") == "da39a3ee5e6b4b0d3255bfef95601890afd80709"
