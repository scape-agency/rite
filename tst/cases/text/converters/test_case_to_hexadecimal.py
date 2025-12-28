# =============================================================================
# Test: case_to_hexadecimal
# =============================================================================

"""
Tests for rite.text.converters.case_to_hexadecimal.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.case_to_hexadecimal import (
    to_hexadecimal_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_hexadecimal_case() -> None:
    """Test to_hexadecimal_case() function."""
    result = to_hexadecimal_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
