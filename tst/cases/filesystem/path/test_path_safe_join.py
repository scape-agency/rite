# =============================================================================
# Test: path_safe_join
# =============================================================================

"""
Tests for rite.filesystem.path.path_safe_join.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.path.path_safe_join import (
    path_safe_join,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_path_safe_join() -> None:
    """Test path_safe_join() with basic path joining."""
    # Basic join
    result = path_safe_join("/var/data", "uploads", "file.txt")
    assert result == "var/data/uploads/file.txt"

    # Single component
    result = path_safe_join("/home/user", "documents")
    assert result == "home/user/documents"

    # Multiple components
    result = path_safe_join("/opt", "app", "data", "file.json")
    assert result == "opt/app/data/file.json"


def test_path_safe_join_traversal_attack() -> None:
    """Test path_safe_join() prevents directory traversal."""
    # Attempt to escape with ../
    with pytest.raises(ValueError, match="outside of the base path"):
        path_safe_join("/var/data", "../etc/passwd")

    # Multiple traversal attempts
    with pytest.raises(ValueError, match="outside of the base path"):
        path_safe_join("/home/user", "../../etc/passwd")


def test_path_safe_join_base_paths() -> None:
    """Test path_safe_join() with various base paths."""
    # Base path without trailing slash
    result = path_safe_join("/usr", "local/bin")
    assert result == "usr/local/bin"

    # Base path with trailing slash
    result = path_safe_join("/usr/", "local/bin")
    assert result == "usr/local/bin"

    # Root path
    result = path_safe_join("/", "etc/config")
    assert result == "etc/config"


def test_path_safe_join_empty_components() -> None:
    """Test path_safe_join() with empty components."""
    # Empty path returns base directory
    result = path_safe_join("/var/data", "")
    assert result == "var/data/"


def test_path_safe_join_special_characters() -> None:
    """Test path_safe_join() with special characters in paths."""
    # Special characters in filenames
    result = path_safe_join("/data", "file-2024.txt")
    assert result == "data/file-2024.txt"

    # Spaces in paths
    result = path_safe_join("/home", "my documents", "file name.txt")
    assert result == "home/my documents/file name.txt"

    # Underscores and dots
    result = path_safe_join("/opt", "_private", ".config")
    assert result == "opt/_private/.config"


def test_path_safe_join_current_directory_references() -> None:
    """Test path_safe_join() with current directory references."""
    # Single dot (current directory)
    result = path_safe_join("/var/data", ".", "file.txt")
    assert "file.txt" in result

    # Multiple dots in path
    result = path_safe_join("/opt", "app.v1", "data")
    assert result == "opt/app.v1/data"


def test_path_safe_join_equals_base() -> None:
    """Test path_safe_join when result equals base (line 75)."""
    # When final path would equal base path, append /
    result = path_safe_join("/var/data", "")
    assert result == "var/data/"


def test_path_safe_join_returns_to_base() -> None:
    """Test path_safe_join when going down then up returns to base (line 75)."""
    # Go into sub-directory then back up with ..
    result = path_safe_join("/var/data", "sub", "..")
    assert result == "var/data/"
