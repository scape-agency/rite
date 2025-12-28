# =============================================================================
# Test: case_to_substitute_numbers_with_words
# =============================================================================

"""
Tests for rite.text.converters.case_to_substitute_numbers_with_words.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.case_to_substitute_numbers_with_words import (
    to_substitute_numbers_with_words_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_substitute_numbers_with_words_case() -> None:
    """Test to_substitute_numbers_with_words_case() function."""
    result = to_substitute_numbers_with_words_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
