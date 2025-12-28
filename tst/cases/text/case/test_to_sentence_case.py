# =============================================================================
# Test: to_sentence_case
# =============================================================================

"""
Tests for rite.text.case.to_sentence_case.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.case.to_sentence_case import (
    to_sentence_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_sentence_case() -> None:
    """Test to_sentence_case() function."""
    result = to_sentence_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
