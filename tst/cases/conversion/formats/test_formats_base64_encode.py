# =============================================================================
# Test: formats_base64_encode
# =============================================================================

"""
Tests for rite.conversion.formats.formats_base64_encode.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.formats.formats_base64_encode import (
    formats_base64_encode,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_formats_base64_encode() -> None:
    """Test formats_base64_encode() function."""
    # Test basic encode with bytes
    assert formats_base64_encode(b"hello") == "aGVsbG8="
    assert formats_base64_encode(b"world") == "d29ybGQ="

    # Test with string
    assert formats_base64_encode("hello") == "aGVsbG8="

    # Test empty
    assert formats_base64_encode(b"") == ""
    assert formats_base64_encode("") == ""
