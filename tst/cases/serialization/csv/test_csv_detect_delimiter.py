# =============================================================================
# Test: csv_detect_delimiter
# =============================================================================

"""
Tests for rite.serialization.csv.csv_detect_delimiter.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.csv.csv_detect_delimiter import (
    csv_detect_delimiter,
)

# =============================================================================
# Test Classes
# =============================================================================


class TestCsvDetectDelimiter:
    """Tests for csv_detect_delimiter()."""

    def test_detect_csv_comma_delimiter(self) -> None:
        """Test detection of comma delimiter for .csv files."""
        assert csv_detect_delimiter("data.csv") == ","

    def test_detect_tsv_tab_delimiter(self) -> None:
        """Test detection of tab delimiter for .tsv files."""
        assert csv_detect_delimiter("data.tsv") == "\t"

    def test_detect_csv_with_path(self) -> None:
        """Test comma detection with file path."""
        assert csv_detect_delimiter("path/to/data.csv") == ","

    def test_detect_tsv_with_path(self) -> None:
        """Test tab detection with file path."""
        assert csv_detect_delimiter("path/to/data.tsv") == "\t"

    def test_detect_unknown_extension_defaults_to_comma(self) -> None:
        """Test that unknown extensions default to comma."""
        assert csv_detect_delimiter("data.txt") == ","
        assert csv_detect_delimiter("data.dat") == ","
        assert csv_detect_delimiter("data") == ","

    def test_detect_case_sensitive_extensions(self) -> None:
        """Test that extension detection is case-sensitive."""
        # Capital extensions should not match
        assert csv_detect_delimiter("data.CSV") == ","
        assert csv_detect_delimiter("data.TSV") == ","

    def test_detect_with_multiple_dots(self) -> None:
        """Test detection with multiple dots in filename."""
        assert csv_detect_delimiter("data.backup.csv") == ","
        assert csv_detect_delimiter("data.backup.tsv") == "\t"

    @pytest.mark.parametrize(
        "filename,expected",
        [
            ("file1.csv", ","),
            ("file2.tsv", "\t"),
            ("./data.csv", ","),
            ("../data.tsv", "\t"),
            ("/absolute/path/data.csv", ","),
            ("/absolute/path/data.tsv", "\t"),
        ],
    )
    def test_detect_various_paths(
        self, filename: str, expected: str
    ) -> None:
        """Test detection with various path formats."""
        assert csv_detect_delimiter(filename) == expected
