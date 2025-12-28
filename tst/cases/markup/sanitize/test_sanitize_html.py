# =============================================================================
# Test: sanitize_html
# =============================================================================

"""
Tests for rite.markup.sanitize.sanitize_html.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.markup.sanitize.sanitize_html import (
    sanitize_html,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_sanitize_html_removes_scripts() -> None:
    """Test that sanitize_html removes script tags."""
    result = sanitize_html("<p>Safe</p><script>alert('xss')</script>")
    assert "script" not in result
    assert "<p>Safe</p>" in result


def test_sanitize_html_allows_default_tags() -> None:
    """Test that sanitize_html allows default tags."""
    result = sanitize_html("<p>Paragraph</p><strong>Bold</strong>")
    assert "<p>Paragraph</p>" in result
    assert "<strong>Bold</strong>" in result


def test_sanitize_html_removes_disallowed_tags() -> None:
    """Test that sanitize_html removes tags not in allowed list."""
    result = sanitize_html("<div>Text</div><p>Para</p>")
    assert "<div>" not in result
    assert "<p>Para</p>" in result


def test_sanitize_html_custom_allowed_tags() -> None:
    """Test sanitize_html with custom allowed tags."""
    result = sanitize_html("<div>Text</div>", allowed_tags=["div"])
    assert "<div>Text</div>" in result


def test_sanitize_html_removes_dangerous_tags() -> None:
    """Test that sanitize_html removes dangerous tags."""
    html = "<iframe src='bad'></iframe><p>Safe</p>"
    result = sanitize_html(html)
    assert "iframe" not in result
    assert "<p>Safe</p>" in result


def test_sanitize_html_handles_attributes() -> None:
    """Test that sanitize_html handles tag attributes."""
    result = sanitize_html('<a href="http://example.com">Link</a>')
    assert "href" in result or "a" in result


def test_sanitize_html_no_allowed_tags() -> None:
    """Test sanitize_html with no allowed tags (branch 69->84)."""
    # Pass empty list - skips tag filtering, only removes dangerous
    result = sanitize_html("<p>Text</p><script>bad</script>", allowed_tags=[])
    # Dangerous tags removed, but other tags remain (no filter applied)
    assert "<p>Text</p>" in result
    assert "script" not in result
