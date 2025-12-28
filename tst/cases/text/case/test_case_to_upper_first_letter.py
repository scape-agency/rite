# =============================================================================
# Test: case_to_upper_first_letter
# =============================================================================

"""
Tests for rite.text.case.case_to_upper_first_letter.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_upper_first_letter import (
    to_upper_first_letter_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_upper_first_letter_case() -> None:
    """Test to_upper_first_letter_case() function."""
    result = to_upper_first_letter_case("hello")
    assert isinstance(result, str)
    assert result[0].isupper()
