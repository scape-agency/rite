# =============================================================================
# Test: sanitize_filename
# =============================================================================

"""
Tests for rite.markup.sanitize.sanitize_filename.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.markup.sanitize.sanitize_filename import (
    sanitize_filename,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_sanitize_filename_basic() -> None:
    """Test sanitize_filename removes unsafe characters."""
    result = sanitize_filename("file:name?.txt")
    assert result == "filename.txt"


def test_sanitize_filename_slashes() -> None:
    """Test sanitize_filename removes forward and back slashes."""
    result = sanitize_filename("my/file\\name.txt")
    assert "/" not in result
    assert "\\" not in result


def test_sanitize_filename_special_chars() -> None:
    """Test sanitize_filename removes special characters."""
    result = sanitize_filename("file<>name|test.txt")
    assert "<" not in result
    assert ">" not in result
    assert "|" not in result


def test_sanitize_filename_quotes() -> None:
    """Test sanitize_filename removes quote characters."""
    result = sanitize_filename('file"name.txt')
    assert '"' not in result


def test_sanitize_filename_with_replacement() -> None:
    """Test sanitize_filename with custom replacement character."""
    result = sanitize_filename("my/file:name.txt", "_")
    assert result == "my_file_name.txt"


def test_sanitize_filename_strips_dots() -> None:
    """Test sanitize_filename strips leading/trailing dots."""
    result = sanitize_filename("...filename.txt...")
    assert result == "filename.txt"


def test_sanitize_filename_strips_spaces() -> None:
    """Test sanitize_filename strips leading/trailing spaces."""
    result = sanitize_filename("  filename.txt  ")
    assert result == "filename.txt"


def test_sanitize_filename_empty_after_sanitization() -> None:
    """Test sanitize_filename returns 'file' when result is empty."""
    result = sanitize_filename(":/\\<>|")
    assert result == "file"


def test_sanitize_filename_preserves_extension() -> None:
    """Test sanitize_filename preserves file extension."""
    result = sanitize_filename("test:file.pdf")
    assert result.endswith(".pdf")


@pytest.mark.parametrize(
    "filename,expected",
    [
        ("normal.txt", "normal.txt"),
        ("file*name.doc", "filename.doc"),
        ("test?.csv", "test.csv"),
    ],
)
def test_sanitize_filename_parametrized(filename: str, expected: str) -> None:
    """Test sanitize_filename with various inputs."""
    result = sanitize_filename(filename)
    assert result == expected
