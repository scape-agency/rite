# =============================================================================
# Test: url_decode
# =============================================================================

"""
Tests for rite.net.url.url_decode.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.net.url.url_decode import (
    url_decode,
)

# =============================================================================
# Test Functions
# =============================================================================


@pytest.mark.parametrize(
    "encoded,expected",
    [
        ("hello%20world", "hello world"),
        ("caf%C3%A9", "café"),
        ("hello+world", "hello+world"),  # Plus is not decoded by unquote
        ("%2F%3F%3D", "/?="),
        ("test%00string", "test\x00string"),
        ("", ""),
        ("no-encoding", "no-encoding"),
        ("%21%40%23", "!@#"),
    ],
)
def test_url_decode(encoded: str, expected: str) -> None:
    """Test url_decode() with various encoded inputs.

    Args:
        encoded: URL-encoded text.
        expected: Expected decoded text.
    """
    result = url_decode(encoded)
    assert result == expected
