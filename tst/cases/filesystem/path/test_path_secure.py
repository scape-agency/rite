# =============================================================================
# Test: path_secure
# =============================================================================

"""
Tests for rite.filesystem.path.path_secure.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.path.path_secure import (
    path_secure,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_path_secure() -> None:
    """Test path_secure() function with traversal prevention."""
    # Test basic secure path
    result = path_secure("/var/data", "file.txt")
    assert result.endswith("file.txt")
    assert "var" in result or "data" in result

    # Test traversal attack prevention - only basename is used
    result = path_secure("/var/data", "../../../etc/passwd")
    assert result.endswith("passwd")
    assert "/etc" not in result

    # Test with complex paths
    result = path_secure("/home/user/uploads", "document.pdf")
    assert result.endswith("document.pdf")

    # Test with trailing slashes
    result1 = path_secure("/var/data", "file.txt")
    result2 = path_secure("/var/data/", "file.txt")
    assert result1 == result2

    # Test with absolute user path - only basename extracted
    result = path_secure("/var/data", "/etc/passwd")
    assert result.endswith("passwd")

    # Test with nested user path - only final component used
    result = path_secure("/uploads", "path/to/deep/file.txt")
    assert result.endswith("file.txt")
