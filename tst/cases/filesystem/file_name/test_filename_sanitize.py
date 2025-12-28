# =============================================================================
# Test: filename_sanitize
# =============================================================================

"""
Tests for rite.filesystem.file_name.filename_sanitize.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.file_name.filename_sanitize import (
    filename_sanitize,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_filename_sanitize() -> None:
    """Test filename_sanitize() function."""
    # Test basic sanitization
    assert filename_sanitize("my file (copy).txt") == "my_file__copy_.txt"
    assert filename_sanitize("document.pdf") == "document.pdf"

    # Test with special characters
    assert filename_sanitize("file:name?.txt") == "file_name_.txt"
    assert filename_sanitize("path/to/file") == "path_to_file"

    # Test with custom replacement character
    assert (
        filename_sanitize("my file (copy).txt", replacement="-")
        == "my-file--copy-.txt"
    )

    # Test max_length parameter
    result = filename_sanitize("a" * 300, max_length=100)
    assert len(result) == 100

    # Test leading/trailing dots and spaces
    assert filename_sanitize(".hidden.txt") == "hidden.txt"
    assert filename_sanitize("  spaced  file.txt") == "__spaced__file.txt"

    # Test empty/invalid filenames
    assert filename_sanitize("!!!") == "___"
    assert filename_sanitize("") == "unnamed"
    assert filename_sanitize("...") == "unnamed"

    # Test alphanumeric, dots, underscores, and hyphens are preserved
    assert filename_sanitize("file-2024_v1.0.txt") == "file-2024_v1.0.txt"
