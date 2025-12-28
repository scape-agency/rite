# =============================================================================
# Test: case_to_first_letter_of_each_word
# =============================================================================

"""
Tests for rite.text.case.case_to_first_letter_of_each_word.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_first_letter_of_each_word import (
    to_first_letter_of_each_word_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_first_letter_of_each_word_case() -> None:
    """Test to_first_letter_of_each_word_case() function."""
    result = to_first_letter_of_each_word_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
