# =============================================================================
# Test: case_to_nato_phonetic_alphabet
# =============================================================================

"""
Tests for rite.text.converters.case_to_nato_phonetic_alphabet.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.case_to_nato_phonetic_alphabet import (
    to_nato_phonetic_alphabet_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_nato_phonetic_alphabet_case() -> None:
    """Test to_nato_phonetic_alphabet_case() function."""
    result = to_nato_phonetic_alphabet_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
