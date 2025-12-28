# =============================================================================
# Test: extension_normalize
# =============================================================================

"""
Tests for rite.filesystem.file_extension.extension_normalize.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.file_extension.extension_normalize import (
    extension_normalize,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_extension_normalize() -> None:
    """Test extension_normalize() function."""
    # Test basic normalization
    assert extension_normalize(".JPG") == "jpg"
    assert extension_normalize("pdf") == "pdf"
    assert extension_normalize(".txt") == "txt"

    # Test with spaces
    assert extension_normalize(" PDF ") == "pdf"
    assert extension_normalize("  .DOC  ") == "doc"

    # Test with multiple dots (compound extensions)
    assert extension_normalize("tar.gz") == "tar.gz"
    assert extension_normalize(".TAR.GZ") == "tar.gz"

    # Test with leading_dot parameter
    assert extension_normalize("jpg", leading_dot=True) == ".jpg"
    assert extension_normalize(".png", leading_dot=True) == ".png"

    # Test None input
    assert extension_normalize(None) is None

    # Test empty and whitespace-only strings
    assert extension_normalize("") is None
    assert extension_normalize("   ") is None
    assert extension_normalize(".") is None
