# =============================================================================
# Test: case_to_abbreviation
# =============================================================================

"""
Tests for rite.text.converters.case_to_abbreviation.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.case_to_abbreviation import (
    to_abbreviation_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_abbreviation_case() -> None:
    """Test to_abbreviation_case() function."""
    result = to_abbreviation_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
