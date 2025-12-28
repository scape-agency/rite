# =============================================================================
# Test: sanitize_clean
# =============================================================================

"""
Tests for rite.text.sanitize.sanitize_clean.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.text.sanitize.sanitize_clean import (
    clean,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_clean() -> None:
    """Test clean() function."""
    result = clean("hello")
    assert isinstance(result, str)
    assert len(result) > 0
