# =============================================================================
# Test: url_encode
# =============================================================================

"""
Tests for rite.net.url.url_encode.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.net.url.url_encode import (
    url_encode,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "text,safe,expected",
    [
        ("hello world", "", "hello%20world"),
        ("café", "", "caf%C3%A9"),
        ("a/b/c", "/", "a/b/c"),
        ("!@#", "", "%21%40%23"),
        ("", "", ""),
        ("hello", "", "hello"),
        ("https://example.com", "https:/.", "https://example.com"),
        ("a=b&c=d", "=&", "a=b&c=d"),
    ],
)
def test_url_encode(text: str, safe: str, expected: str) -> None:
    """Test url_encode() with various inputs.

    Args:
        text: Text to encode.
        safe: Characters not to encode.
        expected: Expected encoded result.
    """
    result = url_encode(text, safe=safe)
    assert result == expected
