# =============================================================================
# Test: case_to_swap
# =============================================================================

"""
Tests for rite.text.case.case_to_swap.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_swap import (
    to_swap_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_swap_case() -> None:
    """Test to_swap_case() function."""
    result = to_swap_case("Hello")
    assert isinstance(result, str)
    assert len(result) == len("Hello")
