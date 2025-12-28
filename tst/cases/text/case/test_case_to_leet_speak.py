# =============================================================================
# Test: case_to_leet_speak
# =============================================================================

"""
Tests for rite.text.case.case_to_leet_speak.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_leet_speak import (
    to_leet_speak_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_leet_speak_case() -> None:
    """Test to_leet_speak_case() function."""
    result = to_leet_speak_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
