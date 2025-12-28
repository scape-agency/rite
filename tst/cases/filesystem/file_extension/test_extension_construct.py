# =============================================================================
# Test: extension_construct
# =============================================================================

"""
Tests for rite.filesystem.file_extension.extension_construct.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.file_extension.extension_construct import (
    extension_construct,
)

# =============================================================================
# Test Functions
# =============================================================================


class TestExtensionConstruct:
    """Tests for extension_construct function."""

    def test_basic_extension(self) -> None:
        """Test basic file extension extraction."""
        assert extension_construct("photo.JPG") == ".jpg"
        assert extension_construct("document.PDF") == ".pdf"
        assert extension_construct("script.py") == ".py"

    def test_compound_extension(self) -> None:
        """Test compound tar extensions."""
        assert extension_construct("archive.tar.gz") == ".tar.gz"
        assert extension_construct("archive.tar.bz2") == ".tar.bz2"
        assert extension_construct("archive.tar.xz") == ".tar.xz"
        assert extension_construct("archive.tar.zst") == ".tar.zst"

    def test_compound_false(self) -> None:
        """Test compound=False returns only last extension."""
        assert extension_construct("archive.tar.gz", compound=False) == ".gz"
        assert extension_construct("archive.tar.bz2", compound=False) == ".bz2"

    def test_hidden_files(self) -> None:
        """Test hidden files have no extension."""
        assert extension_construct(".env") == ""
        assert extension_construct(".gitignore") == ""
        assert extension_construct(".bashrc") == ""

    def test_no_extension(self) -> None:
        """Test files without extension."""
        assert extension_construct("/tmp/noext") == ""
        assert extension_construct("README") == ""
        assert extension_construct("Makefile") == ""

    def test_empty_filename(self) -> None:
        """Test empty filename."""
        assert extension_construct("") == ""

    def test_leading_dot_false(self) -> None:
        """Test leading_dot=False removes leading dot."""
        assert extension_construct("photo.jpg", leading_dot=False) == "jpg"
        assert (
            extension_construct("archive.tar.gz", leading_dot=False)
            == "tar.gz"
        )

    def test_path_with_directories(self) -> None:
        """Test extraction from paths with directories."""
        assert extension_construct("/path/to/file.txt") == ".txt"
        assert extension_construct("./relative/path.json") == ".json"

    def test_multiple_dots(self) -> None:
        """Test files with multiple dots."""
        assert extension_construct("file.backup.txt") == ".txt"
        assert extension_construct("my.file.name.doc") == ".doc"

    def test_whitespace_filename(self) -> None:
        """Test filename with whitespace."""
        assert extension_construct("   ") == ""
        assert extension_construct("  file.txt  ") == ".txt"

    def test_hidden_file_with_extension(self) -> None:
        """Test hidden files with extensions."""
        assert extension_construct(".config.json") == ".json"
