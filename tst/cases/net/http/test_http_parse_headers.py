# =============================================================================
# Test: http_parse_headers
# =============================================================================

"""
Tests for rite.net.http.http_parse_headers.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.net.http.http_parse_headers import (
    http_parse_headers,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_http_parse_headers_single() -> None:
    """Test http_parse_headers with single header."""
    result = http_parse_headers("Content-Type: application/json")
    assert result == {"Content-Type": "application/json"}


def test_http_parse_headers_multiple() -> None:
    """Test http_parse_headers with multiple headers."""
    headers_str = "Content-Type: application/json\r\nHost: example.com"
    result = http_parse_headers(headers_str)
    assert result["Content-Type"] == "application/json"
    assert result["Host"] == "example.com"


def test_http_parse_headers_with_spaces() -> None:
    """Test http_parse_headers handles spaces correctly."""
    result = http_parse_headers("  User-Agent  :  Mozilla/5.0  ")
    assert result["User-Agent"] == "Mozilla/5.0"


def test_http_parse_headers_empty_string() -> None:
    """Test http_parse_headers with empty string."""
    result = http_parse_headers("")
    assert result == {}


def test_http_parse_headers_no_colon() -> None:
    """Test http_parse_headers skips lines without colons."""
    headers_str = (
        "Content-Type: application/json\r\nInvalidLine\r\nHost: example.com"
    )
    result = http_parse_headers(headers_str)
    assert "InvalidLine" not in result
    assert result["Content-Type"] == "application/json"


def test_http_parse_headers_multiple_colons() -> None:
    """Test http_parse_headers handles values with colons."""
    result = http_parse_headers("Authorization: Bearer token:with:colons")
    assert result["Authorization"] == "Bearer token:with:colons"
