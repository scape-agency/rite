# =============================================================================
# Test: random_string
# =============================================================================

"""
Tests for rite.text.random.random_string.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.random.random_string import (
    random_string,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_random_string() -> None:
    """Test random_string() function."""
    result = random_string(10)
    assert isinstance(result, str)
    assert len(result) == 10
