# =============================================================================
# Test: uuid_is_valid
# =============================================================================

"""
Tests for rite.crypto.uuid.uuid_is_valid.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.uuid.uuid_is_valid import (
    is_valid_uuid,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_is_valid_uuid() -> None:
    """Test is_valid_uuid() function."""
    # Valid UUID v4
    assert is_valid_uuid("550e8400-e29b-41d4-a716-446655440000") is True

    # Invalid UUID (not UUID format)
    assert is_valid_uuid("invalid") is False
    assert is_valid_uuid("not-a-uuid") is False

    # Invalid UUID (wrong format)
    assert is_valid_uuid("550e8400-e29b-41d4-a716") is False

    # Empty string
    assert is_valid_uuid("") is False
