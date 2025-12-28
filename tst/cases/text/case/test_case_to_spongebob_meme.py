# =============================================================================
# Test: case_to_spongebob_meme
# =============================================================================

"""
Tests for rite.text.case.case_to_spongebob_meme.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.case_to_spongebob_meme import (
    to_spongebob_meme_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_spongebob_meme_case() -> None:
    """Test to_spongebob_meme_case() function."""
    result = to_spongebob_meme_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
