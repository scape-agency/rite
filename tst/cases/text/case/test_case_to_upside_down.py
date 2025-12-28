# =============================================================================
# Test: case_to_upside_down
# =============================================================================

"""
Tests for rite.text.case.case_to_upside_down.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_upside_down import (
    to_upside_down_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_upside_down_case() -> None:
    """Test to_upside_down_case() function."""
    result = to_upside_down_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
