# =============================================================================
# Test: validation_is_url
# =============================================================================

"""
Tests for rite.net.validation.validation_is_url.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.net.validation.validation_is_url import (
    validation_is_url,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "url,require_scheme,expected",
    [
        ("https://example.com", True, True),
        ("http://example.com", True, True),
        ("https://sub.example.com", True, True),
        ("https://example.com:8080", True, True),
        ("https://example.com/path", True, True),
        ("https://localhost", True, True),
        ("https://192.168.1.1", True, True),
        ("not a url", True, False),
        ("ftp://example.com", True, False),
        ("example.com", True, False),
        ("example.com", False, True),
        ("sub.example.com/path", False, True),
        ("", True, False),
        ("https://", True, False),
    ],
)
def test_validation_is_url(
    url: str, require_scheme: bool, expected: bool
) -> None:
    """Test validation_is_url() with various URL formats.

    Args:
        url: URL to validate.
        require_scheme: Whether scheme is required.
        expected: Whether URL is valid.
    """
    result = validation_is_url(url, require_scheme=require_scheme)
    assert result == expected
