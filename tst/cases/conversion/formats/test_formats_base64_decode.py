# =============================================================================
# Test: formats_base64_decode
# =============================================================================

"""
Tests for rite.conversion.formats.formats_base64_decode.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.conversion.formats.formats_base64_decode import (
    formats_base64_decode,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_formats_base64_decode() -> None:
    """Test formats_base64_decode() function."""
    # Test basic decode
    assert formats_base64_decode("aGVsbG8=") == b"hello"
    assert formats_base64_decode("d29ybGQ=") == b"world"

    # Test empty string
    assert formats_base64_decode("") == b""

    # Test with padding
    assert formats_base64_decode("YQ==") == b"a"
