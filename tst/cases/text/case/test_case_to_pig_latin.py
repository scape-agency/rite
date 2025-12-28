# =============================================================================
# Test: case_to_pig_latin
# =============================================================================

"""
Tests for rite.text.case.case_to_pig_latin.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_pig_latin import (
    to_pig_latin_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_pig_latin_case() -> None:
    """Test to_pig_latin_case() function."""
    result = to_pig_latin_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
