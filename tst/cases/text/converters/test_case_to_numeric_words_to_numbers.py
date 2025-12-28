# =============================================================================
# Test: case_to_numeric_words_to_numbers
# =============================================================================

"""
Tests for rite.text.converters.case_to_numeric_words_to_numbers.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.case_to_numeric_words_to_numbers import (
    to_numeric_words_to_numbers_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_numeric_words_to_numbers_case() -> None:
    """Test to_numeric_words_to_numbers_case() function."""
    result = to_numeric_words_to_numbers_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
