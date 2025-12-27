# =============================================================================
# Test: random_int
# =============================================================================

"""
Tests for rite.crypto.random.random_int.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.crypto.random.random_int import (
    random_int,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_random_int() -> None:
    """Test random_int() function."""
    # Test range
    for _ in range(10):
        result = random_int(0, 100)
        assert 0 <= result <= 100
    
    # Test different range
    for _ in range(10):
        result = random_int(50, 60)
        assert 50 <= result <= 60
    
    # Test uniqueness
    results = [random_int(0, 1000) for _ in range(20)]
    assert len(set(results)) > 1  # Should have variety
