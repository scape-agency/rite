# =============================================================================
# Test: case_to_alphabet_position
# =============================================================================

"""
Tests for rite.text.case.case_to_alphabet_position.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_alphabet_position import (
    to_alphabet_position_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_alphabet_position_case() -> None:
    """Test to_alphabet_position_case() function."""
    result = to_alphabet_position_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
