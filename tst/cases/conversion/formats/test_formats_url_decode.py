# =============================================================================
# Test: formats_url_decode
# =============================================================================

"""
Tests for rite.conversion.formats.formats_url_decode.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.formats.formats_url_decode import (
    formats_url_decode,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_formats_url_decode() -> None:
    """Test formats_url_decode() function."""
    # Test basic decode
    assert formats_url_decode("hello%20world") == "hello world"
    assert formats_url_decode("test%2Bvalue") == "test+value"
    assert formats_url_decode("a%3Db") == "a=b"

    # Test no encoding
    assert formats_url_decode("hello") == "hello"
