# =============================================================================
# Test: case_to_slug
# =============================================================================

"""
Tests for rite.text.case.case_to_slug.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_slug import (
    to_slug_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_slug_case() -> None:
    """Test to_slug_case() function."""
    result = to_slug_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
