# =============================================================================
# Test: to_title_case
# =============================================================================

"""
Tests for rite.text.case.to_title_case.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.to_title_case import (
    to_title_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_title_case() -> None:
    """Test to_title_case() function."""
    result = to_title_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
