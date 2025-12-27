# =============================================================================
# Test: hash_sha384
# =============================================================================

"""
Tests for rite.crypto.hash.hash_sha384.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.hash.hash_sha384 import (
    hash_sha384,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_hash_sha384() -> None:
    """Test hash_sha384() function."""
    # Test with string
    result = hash_sha384("hello")
    assert len(result) == 96  # sha384 produces 48 bytes = 96 hex chars
    assert (
        result
        == "59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f"
    )

    # Test with bytes
    assert hash_sha384(b"hello") == result

    # Test empty string
    result_empty = hash_sha384("")
    assert len(result_empty) == 96
