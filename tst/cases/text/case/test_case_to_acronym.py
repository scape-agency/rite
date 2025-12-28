# =============================================================================
# Test: case_to_acronym
# =============================================================================

"""
Tests for rite.text.case.case_to_acronym.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_acronym import (
    to_acronym_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_acronym_case() -> None:
    """Test to_acronym_case() function."""
    assert to_acronym_case("Random Access Memory") == "RAM"
    assert to_acronym_case("Hyper Text Markup Language") == "HTML"
    assert to_acronym_case("") == ""
    assert to_acronym_case("hello world") == "HW"
