# =============================================================================
# Test: case_to_double_every_second_word
# =============================================================================

"""
Tests for rite.text.converters.case_to_double_every_second_word.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.case_to_double_every_second_word import (
    to_double_every_second_word_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_double_every_second_word_case() -> None:
    """Test to_double_every_second_word_case() function."""
    result = to_double_every_second_word_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
