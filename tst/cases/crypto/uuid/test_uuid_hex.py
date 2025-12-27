# =============================================================================
# Test: uuid_hex
# =============================================================================

"""
Tests for rite.crypto.uuid.uuid_hex.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.uuid.uuid_hex import (
    uuid_hex,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_uuid_hex() -> None:
    """Test uuid_hex() function."""
    # Test basic generation
    result = uuid_hex()
    assert isinstance(result, str)
    assert len(result) == 32  # UUID hex format (no dashes)
    assert all(c in "0123456789abcdef" for c in result)

    # Test uniqueness
    result1 = uuid_hex()
    result2 = uuid_hex()
    assert result1 != result2
