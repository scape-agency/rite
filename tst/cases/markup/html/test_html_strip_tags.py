# =============================================================================
# Test: html_strip_tags
# =============================================================================

"""
Tests for rite.markup.html.html_strip_tags.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.markup.html.html_strip_tags import (
    html_strip_tags,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_html_strip_tags_single_tag() -> None:
    """Test html_strip_tags removes single tag."""
    html = "<div>Keep</div><style>Remove</style>"
    result = html_strip_tags(html, ["style"])
    assert "<style>" not in result
    assert "Remove" not in result
    assert "<div>Keep</div>" in result


def test_html_strip_tags_multiple_tags() -> None:
    """Test html_strip_tags removes multiple tags."""
    html = "<p>Keep</p><script>Alert</script><style>CSS</style>"
    result = html_strip_tags(html, ["script", "style"])
    assert "<script>" not in result
    assert "<style>" not in result
    assert "Alert" not in result
    assert "CSS" not in result
    assert "<p>Keep</p>" in result


def test_html_strip_tags_case_insensitive() -> None:
    """Test html_strip_tags is case-insensitive."""
    html = "<SCRIPT>alert()</SCRIPT>"
    result = html_strip_tags(html, ["script"])
    assert "alert" not in result


def test_html_strip_tags_with_attributes() -> None:
    """Test html_strip_tags removes tags with attributes."""
    html = '<script type="text/javascript">code()</script>'
    result = html_strip_tags(html, ["script"])
    assert "<script" not in result
    assert "code" not in result


def test_html_strip_tags_no_tags_to_remove() -> None:
    """Test html_strip_tags with empty tag list."""
    html = "<p>Content</p>"
    result = html_strip_tags(html, [])
    assert result == html


def test_html_strip_tags_no_matching_tags() -> None:
    """Test html_strip_tags when no matching tags found."""
    html = "<p>Content</p>"
    result = html_strip_tags(html, ["script"])
    assert result == html


def test_html_strip_tags_nested_content() -> None:
    """Test html_strip_tags with nested tags."""
    html = "<div><p>Keep</p></div><script><code>Remove</code></script>"
    result = html_strip_tags(html, ["script"])
    assert "Keep" in result
    assert "Remove" not in result
    assert "<code>" not in result


def test_html_strip_tags_empty_string() -> None:
    """Test html_strip_tags with empty HTML."""
    result = html_strip_tags("", ["script"])
    assert result == ""
