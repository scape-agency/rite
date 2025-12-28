# =============================================================================
# Test: mimetype_match
# =============================================================================

"""
Tests for rite.filesystem.mimetype.mimetype_match.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.mimetype.mimetype_match import mimetype_match

# =============================================================================
# Test Functions
# =============================================================================


def test_mimetype_match_exact_and_wildcard() -> None:
    """Test exact matches and wildcard pattern matching."""
    assert mimetype_match("image/png", "image/png")
    assert mimetype_match("image/jpeg", "image/*")
    assert not mimetype_match("text/plain", "image/*")
