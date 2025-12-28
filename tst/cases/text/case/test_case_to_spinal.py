# =============================================================================
# Test: case_to_spinal
# =============================================================================

"""
Tests for rite.text.case.case_to_spinal.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_spinal import (
    to_spinal_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_spinal_case() -> None:
    """Test to_spinal_case() function."""
    result = to_spinal_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
