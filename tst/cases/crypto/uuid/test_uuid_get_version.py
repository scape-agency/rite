# =============================================================================
# Test: uuid_get_version
# =============================================================================

"""
Tests for rite.crypto.uuid.uuid_get_version.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.uuid.uuid_get_version import (
    get_version,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_get_version() -> None:
    """Test get_version() function."""
    # Import | Standard Library
    import uuid as stdlib_uuid

    # Test UUID v4
    uuid_v4 = stdlib_uuid.uuid4()
    assert get_version(uuid_v4) == 4

    # Test UUID v5
    uuid_v5 = stdlib_uuid.uuid5(stdlib_uuid.NAMESPACE_DNS, "example.com")
    assert get_version(uuid_v5) == 5

    # Test UUID v3
    uuid_v3 = stdlib_uuid.uuid3(stdlib_uuid.NAMESPACE_DNS, "example.com")
    assert get_version(uuid_v3) == 3
