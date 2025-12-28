# =============================================================================
# Test: case_to_spongebob_mocking
# =============================================================================

"""
Tests for rite.text.case.case_to_spongebob_mocking.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_spongebob_mocking import (
    to_mocking_spongebob_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_mocking_spongebob_case() -> None:
    """Test to_mocking_spongebob_case() function."""
    result = to_mocking_spongebob_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
