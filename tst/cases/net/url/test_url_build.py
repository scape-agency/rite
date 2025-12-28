# =============================================================================
# Test: url_build
# =============================================================================

"""
Tests for rite.net.url.url_build.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.net.url.url_build import (
    url_build,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_url_build() -> None:
    """Test url_build() function."""
    # Test basic URL
    assert url_build("https", "example.com") == "https://example.com"
    assert url_build("http", "test.com") == "http://test.com"

    # Test with path
    assert (
        url_build("https", "example.com", "/path")
        == "https://example.com/path"
    )
    assert (
        url_build("https", "example.com", "/api/v1")
        == "https://example.com/api/v1"
    )

    # Test with query as string
    assert (
        url_build("https", "example.com", query="q=1")
        == "https://example.com?q=1"
    )
    assert (
        url_build("http", "test.com", "/search", query="q=test&lang=en")
        == "http://test.com/search?q=test&lang=en"
    )

    # Test with query as dict
    assert (
        url_build("https", "example.com", query={"q": "1"})
        == "https://example.com?q=1"
    )
    assert (
        url_build("http", "test.com", query={"a": "1", "b": "2"})
        == "http://test.com?a=1&b=2"
    )

    # Test with fragment
    assert (
        url_build("https", "example.com", fragment="section")
        == "https://example.com#section"
    )
    assert (
        url_build("https", "example.com", "/page", fragment="top")
        == "https://example.com/page#top"
    )

    # Test with all components
    result = url_build(
        "https", "example.com", "/path", query="q=1", fragment="results"
    )
    assert result == "https://example.com/path?q=1#results"

    # Test with port
    assert url_build("https", "example.com:8080") == "https://example.com:8080"
    assert (
        url_build("http", "localhost:3000", "/api")
        == "http://localhost:3000/api"
    )

    # Test empty components
    assert url_build() == ""
    assert url_build(scheme="https") == "https://"

    # Test complex query dict
    assert (
        url_build(
            "https", "example.com", query={"key1": "value1", "key2": "value2"}
        )
        == "https://example.com?key1=value1&key2=value2"
    )
