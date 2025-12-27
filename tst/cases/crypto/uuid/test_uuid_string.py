# =============================================================================
# Test: uuid_string
# =============================================================================

"""
Tests for rite.crypto.uuid.uuid_string.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.uuid.uuid_string import (
    uuid_string,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_uuid_string() -> None:
    """Test uuid_string() function."""
    # Test basic generation
    result = uuid_string()
    assert isinstance(result, str)
    assert len(result) == 36  # UUID string format: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    assert result.count("-") == 4
    
    # Test uniqueness
    result1 = uuid_string()
    result2 = uuid_string()
    assert result1 != result2
