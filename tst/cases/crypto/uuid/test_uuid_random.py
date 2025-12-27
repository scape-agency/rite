# =============================================================================
# Test: uuid_random
# =============================================================================

"""
Tests for rite.crypto.uuid.uuid_random.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.uuid.uuid_random import (
    uuid_random,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_uuid_random() -> None:
    """Test uuid_random() function."""
    import uuid as stdlib_uuid
    
    # Test basic generation
    result = uuid_random()
    assert isinstance(result, stdlib_uuid.UUID)
    
    # Test uniqueness
    result1 = uuid_random()
    result2 = uuid_random()
    assert result1 != result2
    
    # Test version 4 (random)
    assert result.version == 4
