# =============================================================================
# Test: url_parse
# =============================================================================

"""
Tests for rite.net.url.url_parse.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.net.url.url_parse import (
    url_parse,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_url_parse() -> None:
    """Test url_parse() with standard URL."""
    result = url_parse("https://example.com:8080/path?q=1#frag")
    assert result.scheme == "https"
    assert result.netloc == "example.com:8080"
    assert result.path == "/path"
    assert result.query == "q=1"
    assert result.fragment == "frag"


def test_url_parse_simple() -> None:
    """Test url_parse() with simple URL."""
    result = url_parse("http://example.com/path")
    assert result.scheme == "http"
    assert result.netloc == "example.com"
    assert result.path == "/path"
    assert result.query == ""
    assert result.fragment == ""


def test_url_parse_no_scheme() -> None:
    """Test url_parse() with relative URL."""
    result = url_parse("/path/to/resource")
    assert result.scheme == ""
    assert result.path == "/path/to/resource"


def test_url_parse_with_port() -> None:
    """Test url_parse() with port number."""
    result = url_parse("http://localhost:3000")
    assert result.scheme == "http"
    assert result.netloc == "localhost:3000"
    assert result.hostname == "localhost"
    assert result.port == 3000
