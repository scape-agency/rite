# =============================================================================
# Test: case_to_upper_vowel
# =============================================================================

"""
Tests for rite.text.case.case_to_upper_vowel.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_upper_vowel import (
    to_vowel_uppercase_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_vowel_uppercase_case() -> None:
    """Test to_vowel_uppercase_case() function."""
    result = to_vowel_uppercase_case("hello")
    assert isinstance(result, str)
    assert len(result) == len("hello")
