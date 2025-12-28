# =============================================================================
# Test: case_to_numeronym
# =============================================================================

"""
Tests for rite.text.converters.case_to_numeronym.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.case_to_numeronym import (
    to_numeronym_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_numeronym_case() -> None:
    """Test to_numeronym_case() function."""
    result = to_numeronym_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
