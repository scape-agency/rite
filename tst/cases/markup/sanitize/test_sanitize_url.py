# =============================================================================
# Test: sanitize_url
# =============================================================================

"""
Tests for rite.markup.sanitize.sanitize_url.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.markup.sanitize.sanitize_url import (
    sanitize_url,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_sanitize_url_valid_http() -> None:
    """Test sanitize_url with valid HTTP URL."""
    result = sanitize_url("http://example.com")
    assert result == "http://example.com"


def test_sanitize_url_valid_https() -> None:
    """Test sanitize_url with valid HTTPS URL."""
    result = sanitize_url("https://example.com")
    assert result == "https://example.com"


def test_sanitize_url_javascript_blocked() -> None:
    """Test sanitize_url blocks javascript: scheme."""
    result = sanitize_url("javascript:alert('xss')")
    assert result == ""


def test_sanitize_url_data_blocked() -> None:
    """Test sanitize_url blocks data: scheme."""
    result = sanitize_url("data:text/html,<script>alert()</script>")
    assert result == ""


def test_sanitize_url_custom_scheme() -> None:
    """Test sanitize_url with custom allowed schemes."""
    result = sanitize_url("ftp://server.com", ["ftp"])
    assert result == "ftp://server.com"


def test_sanitize_url_custom_scheme_blocked() -> None:
    """Test sanitize_url blocks non-allowed custom schemes."""
    result = sanitize_url("ftp://server.com", ["http"])
    assert result == ""


def test_sanitize_url_invalid_format() -> None:
    """Test sanitize_url with invalid URL format."""
    result = sanitize_url("not a valid url")
    assert result == ""


def test_sanitize_url_empty_string() -> None:
    """Test sanitize_url with empty string."""
    result = sanitize_url("")
    assert result == ""


@pytest.mark.parametrize(
    "url,allowed,expected",
    [
        ("https://test.com", ["https"], "https://test.com"),
        ("http://test.com", ["https"], ""),
        ("ftp://test.com", ["http", "https"], ""),
        ("https://Test.com", ["HTTPS"], "https://Test.com"),
    ],
)
def test_sanitize_url_parametrized(
    url: str, allowed: list[str], expected: str
) -> None:
    """Test sanitize_url with various parameters."""
    result = sanitize_url(url, allowed)
    assert result == expected


def test_sanitize_url_exception_handling() -> None:
    """Test sanitize_url handles exceptions gracefully (line 67)."""
    # A URL that might cause issues during parsing but shouldn't crash
    result = sanitize_url("://broken", ["http"])
    assert result == ""


def test_sanitize_url_exception_from_urlparse() -> None:
    """Test sanitize_url exception handler (line 67)."""
    # Import | Standard Library
    from unittest.mock import patch

    # Mock urlparse to raise an exception
    with patch(
        "rite.markup.sanitize.sanitize_url.urlparse",
        side_effect=ValueError("parse error"),
    ):
        result = sanitize_url("https://test.com")
        assert result == ""
