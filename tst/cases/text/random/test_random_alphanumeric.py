# =============================================================================
# Test: random_alphanumeric
# =============================================================================

"""
Tests for rite.text.random.random_alphanumeric.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.random.random_alphanumeric import (
    random_alphanumeric,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_random_alphanumeric() -> None:
    """Test random_alphanumeric() function."""
    result = random_alphanumeric(10)
    assert isinstance(result, str)
    assert len(result) == 10