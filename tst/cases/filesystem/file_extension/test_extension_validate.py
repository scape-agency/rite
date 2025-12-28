# =============================================================================
# Test: extension_validate
# =============================================================================

"""
Tests for rite.filesystem.file_extension.extension_validate.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.file_extension.extension_validate import (
    extension_validate,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_extension_validate() -> None:
    """Test extension_validate() function."""
    # Valid extensions should not raise
    extension_validate("pdf")
    extension_validate("jpg")
    extension_validate("txt")

    # Test with allowed list
    extension_validate("jpg", allowed=["jpg", "png", "gif"])
    extension_validate("PNG", allowed=["jpg", "png", "gif"])

    # Invalid: None
    with pytest.raises(ValueError, match="empty or None"):
        extension_validate(None)

    # Invalid: empty string
    with pytest.raises(ValueError, match="empty or None"):
        extension_validate("")

    # Invalid: not in allowed list
    with pytest.raises(ValueError, match="not allowed"):
        extension_validate("exe", allowed=["jpg", "png", "gif"])

    # Invalid: doesn't match regex
    with pytest.raises(ValueError, match="Invalid file extension"):
        extension_validate("!!!invalid!!!")
