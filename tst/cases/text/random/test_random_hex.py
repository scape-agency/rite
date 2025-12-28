# =============================================================================
# Test: random_hex
# =============================================================================

"""
Tests for rite.text.random.random_hex.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.random.random_hex import (
    random_hex,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_random_hex() -> None:
    """Test random_hex() function."""
    result = random_hex(8)
    assert isinstance(result, str)
    assert len(result) == 8
