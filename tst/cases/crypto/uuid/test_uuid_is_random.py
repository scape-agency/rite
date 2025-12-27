# =============================================================================
# Test: uuid_is_random
# =============================================================================

"""
Tests for rite.crypto.uuid.uuid_is_random.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.uuid.uuid_is_random import (
    is_random_uuid,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_is_random_uuid() -> None:
    """Test is_random_uuid() function."""
    # Import | Standard Library
    import uuid as stdlib_uuid

    # Test UUID v4 (random)
    uuid_v4 = stdlib_uuid.uuid4()
    assert is_random_uuid(uuid_v4) is True

    # Test UUID v5 (name-based)
    uuid_v5 = stdlib_uuid.uuid5(stdlib_uuid.NAMESPACE_DNS, "example.com")
    assert is_random_uuid(uuid_v5) is False

    # Test UUID v3 (name-based)
    uuid_v3 = stdlib_uuid.uuid3(stdlib_uuid.NAMESPACE_DNS, "example.com")
    assert is_random_uuid(uuid_v3) is False
