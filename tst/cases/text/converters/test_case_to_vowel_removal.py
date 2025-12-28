# =============================================================================
# Test: case_to_vowel_removal
# =============================================================================

"""
Tests for rite.text.converters.case_to_vowel_removal.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.case_to_vowel_removal import (
    to_vowel_removal_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_vowel_removal_case() -> None:
    """Test to_vowel_removal_case() function."""
    result = to_vowel_removal_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
