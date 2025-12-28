# =============================================================================
# Test: http_status_code
# =============================================================================

"""
Tests for rite.net.http.http_status_code.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.net.http.http_status_code import (
    http_status_code,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_http_status_code() -> None:
    """Test http_status_code() function."""
    # Test 2xx codes
    assert http_status_code(200) == "OK"
    assert http_status_code(201) == "Created"
    assert http_status_code(202) == "Accepted"
    assert http_status_code(204) == "No Content"

    # Test 3xx codes
    assert http_status_code(300) == "Multiple Choices"
    assert http_status_code(301) == "Moved Permanently"
    assert http_status_code(302) == "Found"
    assert http_status_code(304) == "Not Modified"

    # Test 4xx codes
    assert http_status_code(400) == "Bad Request"
    assert http_status_code(401) == "Unauthorized"
    assert http_status_code(403) == "Forbidden"
    assert http_status_code(404) == "Not Found"
    assert http_status_code(405) == "Method Not Allowed"

    # Test 5xx codes
    assert http_status_code(500) == "Internal Server Error"
    assert http_status_code(501) == "Not Implemented"
    assert http_status_code(502) == "Bad Gateway"
    assert http_status_code(503) == "Service Unavailable"

    # Test invalid codes
    assert http_status_code(999) == "Unknown Status"
    assert http_status_code(600) == "Unknown Status"
    assert http_status_code(-1) == "Unknown Status"
