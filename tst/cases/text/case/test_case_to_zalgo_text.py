# =============================================================================
# Test: case_to_zalgo_text
# =============================================================================

"""
Tests for rite.text.case.case_to_zalgo_text.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_zalgo_text import (
    to_zalgo_text_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_zalgo_text_case() -> None:
    """Test to_zalgo_text_case() function."""
    result = to_zalgo_text_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
