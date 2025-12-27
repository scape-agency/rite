# =============================================================================
# Test: uuid_from_name
# =============================================================================

"""
Tests for rite.crypto.uuid.uuid_from_name.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.uuid.uuid_from_name import (
    from_name,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_from_name() -> None:
    """Test from_name() function."""
    # Import | Standard Library
    import uuid as stdlib_uuid

    # Test basic generation with DNS namespace
    result = from_name(stdlib_uuid.NAMESPACE_DNS, "example.com")
    assert isinstance(result, stdlib_uuid.UUID)
    assert result.version == 5  # UUID v5 uses SHA-1

    # Test deterministic behavior (same input = same output)
    result1 = from_name(stdlib_uuid.NAMESPACE_DNS, "example.com")
    result2 = from_name(stdlib_uuid.NAMESPACE_DNS, "example.com")
    assert result1 == result2

    # Test different names produce different UUIDs
    result3 = from_name(stdlib_uuid.NAMESPACE_DNS, "different.com")
    assert result1 != result3
