# =============================================================================
# Test: case_to_random
# =============================================================================

"""
Tests for rite.text.case.case_to_random.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_random import (
    to_random_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_random_case() -> None:
    """Test to_random_case() function."""
    result = to_random_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
