# =============================================================================
# Test: http_is_method
# =============================================================================

"""
Tests for rite.net.http.http_is_method.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.net.http.http_is_method import (
    http_is_method,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_http_is_method() -> None:
    """Test http_is_method() function."""
    # Test valid HTTP methods
    assert http_is_method("GET") is True
    assert http_is_method("POST") is True
    assert http_is_method("PUT") is True
    assert http_is_method("DELETE") is True
    assert http_is_method("PATCH") is True
    assert http_is_method("HEAD") is True
    assert http_is_method("OPTIONS") is True
    assert http_is_method("TRACE") is True

    # Test case insensitivity
    assert http_is_method("get") is True
    assert http_is_method("Get") is True
    assert http_is_method("post") is True
    assert http_is_method("Post") is True

    # Test invalid methods
    assert http_is_method("INVALID") is False
    assert http_is_method("CONNECT") is False
    assert http_is_method("CUSTOM") is False
    assert http_is_method("") is False

    # Test lowercase invalid
    assert http_is_method("invalid") is False

    # Test single letter
    assert http_is_method("G") is False

    # Test numeric
    assert http_is_method("123") is False

    # Test with spaces
    assert http_is_method("GET ") is False
    assert http_is_method(" GET") is False
