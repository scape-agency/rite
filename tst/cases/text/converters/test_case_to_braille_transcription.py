# =============================================================================
# Test: case_to_braille_transcription
# =============================================================================

"""
Tests for rite.text.converters.case_to_braille_transcription.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.converters.case_to_braille_transcription import (
    to_braille_transcription_case,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_to_braille_transcription_case() -> None:
    """Test to_braille_transcription_case() function."""
    result = to_braille_transcription_case("hello")
    assert isinstance(result, str)
    assert len(result) > 0
