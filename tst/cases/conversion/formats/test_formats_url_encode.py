# =============================================================================
# Test: formats_url_encode
# =============================================================================

"""
Tests for rite.conversion.formats.formats_url_encode.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.formats.formats_url_encode import (
    formats_url_encode,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_formats_url_encode() -> None:
    """Test formats_url_encode() function."""
    # Test basic encode (quote_plus uses + for spaces)
    assert formats_url_encode("hello world") == "hello+world"
    assert formats_url_encode("test+value") == "test%2Bvalue"
    assert formats_url_encode("a=b") == "a%3Db"

    # Test no encoding needed
    assert formats_url_encode("hello") == "hello"

    # Test with safe parameter
    assert formats_url_encode("a/b", safe="/") == "a/b"
