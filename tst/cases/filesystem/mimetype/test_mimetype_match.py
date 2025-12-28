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


def test_mimetype_match_empty_inputs() -> None:
    """Test empty string inputs return False."""
    assert not mimetype_match("", "image/png")
    assert not mimetype_match("image/png", "")
    assert not mimetype_match("", "")


def test_mimetype_match_case_insensitive() -> None:
    """Test matching is case-insensitive."""
    assert mimetype_match("IMAGE/PNG", "image/png")
    assert mimetype_match("image/png", "IMAGE/PNG")
    assert mimetype_match("Image/Jpeg", "image/*")


def test_mimetype_match_with_whitespace() -> None:
    """Test matching handles whitespace."""
    assert mimetype_match("  image/png  ", "image/png")
    assert mimetype_match("image/png", "  image/png  ")


def test_mimetype_match_no_match() -> None:
    """Test non-matching patterns."""
    assert not mimetype_match("image/png", "application/json")
    assert not mimetype_match("text/html", "image/png")
