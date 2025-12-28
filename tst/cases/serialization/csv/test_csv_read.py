# =============================================================================
# Test: csv_read
# =============================================================================

"""
Tests for rite.serialization.csv.csv_read.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.csv.csv_read import (
    csv_read,
)

# =============================================================================
# Test Classes
# =============================================================================


class TestCsvRead:
    """Tests for csv_read()."""

    def test_read_basic_csv(self, tmp_path: Path) -> None:
        """Test reading a basic CSV file."""
        # Create a test CSV file
        csv_file = tmp_path / "test.csv"
        csv_file.write_text("name,age,city\nAlice,30,NYC\nBob,25,LA\n")

        # Read the CSV
        result = csv_read(csv_file)

        # Verify results
        assert len(result) == 2
        assert result[0] == {"name": "Alice", "age": "30", "city": "NYC"}
        assert result[1] == {"name": "Bob", "age": "25", "city": "LA"}

    def test_read_tsv_with_delimiter(self, tmp_path: Path) -> None:
        """Test reading a TSV file with tab delimiter."""
        # Create a test TSV file
        tsv_file = tmp_path / "test.tsv"
        tsv_file.write_text("name\tage\tcity\nAlice\t30\tNYC\nBob\t25\tLA\n")

        # Read the TSV
        result = csv_read(tsv_file, delimiter="\t")

        # Verify results
        assert len(result) == 2
        assert result[0] == {"name": "Alice", "age": "30", "city": "NYC"}
        assert result[1] == {"name": "Bob", "age": "25", "city": "LA"}

    def test_read_csv_with_string_path(self, tmp_path: Path) -> None:
        """Test reading CSV using string path."""
        # Create a test CSV file
        csv_file = tmp_path / "test.csv"
        csv_file.write_text("id,value\n1,test\n")

        # Read using string path
        result = csv_read(str(csv_file))

        assert len(result) == 1
        assert result[0] == {"id": "1", "value": "test"}

    def test_read_csv_with_path_object(self, tmp_path: Path) -> None:
        """Test reading CSV using Path object."""
        # Create a test CSV file
        csv_file = tmp_path / "test.csv"
        csv_file.write_text("id,value\n1,test\n")

        # Read using Path object
        result = csv_read(csv_file)

        assert len(result) == 1
        assert result[0] == {"id": "1", "value": "test"}

    def test_read_empty_csv_with_header_only(self, tmp_path: Path) -> None:
        """Test reading CSV with only header row."""
        # Create a CSV with header only
        csv_file = tmp_path / "empty.csv"
        csv_file.write_text("name,age,city\n")

        # Read the CSV
        result = csv_read(csv_file)

        # Should return empty list
        assert result == []

    def test_read_csv_with_special_characters(self, tmp_path: Path) -> None:
        """Test reading CSV with special characters and quotes."""
        # Create CSV with special characters
        csv_file = tmp_path / "special.csv"
        csv_file.write_text(
            "name,description\n"
            'Item "A","Contains, comma"\n'
            'Item B,"Contains ""quotes"""\n'
        )

        # Read the CSV
        result = csv_read(csv_file)

        assert len(result) == 2
        assert result[0]["name"] == 'Item "A"'
        assert result[0]["description"] == "Contains, comma"
        assert result[1]["name"] == "Item B"
        assert result[1]["description"] == 'Contains "quotes"'

    def test_read_csv_with_empty_fields(self, tmp_path: Path) -> None:
        """Test reading CSV with empty field values."""
        # Create CSV with empty fields
        csv_file = tmp_path / "empty_fields.csv"
        csv_file.write_text(
            "name,email,phone\nAlice,alice@test.com,\nBob,,555-1234\n"
        )

        # Read the CSV
        result = csv_read(csv_file)

        assert len(result) == 2
        assert result[0]["phone"] == ""
        assert result[1]["email"] == ""

    def test_read_csv_with_unicode(self, tmp_path: Path) -> None:
        """Test reading CSV with Unicode characters."""
        # Create CSV with Unicode
        csv_file = tmp_path / "unicode.csv"
        csv_file.write_text(
            "name,greeting\nAlice,Hello\nBöb,Hallö\nJosé,¡Hola!\n"
        )

        # Read the CSV
        result = csv_read(csv_file)

        assert len(result) == 3
        assert result[1]["name"] == "Böb"
        assert result[2]["greeting"] == "¡Hola!"

    def test_read_csv_with_semicolon_delimiter(self, tmp_path: Path) -> None:
        """Test reading CSV with semicolon delimiter."""
        # Create CSV with semicolon delimiter
        csv_file = tmp_path / "semicolon.csv"
        csv_file.write_text("name;age;city\nAlice;30;NYC\n")

        # Read the CSV
        result = csv_read(csv_file, delimiter=";")

        assert len(result) == 1
        assert result[0] == {"name": "Alice", "age": "30", "city": "NYC"}

    def test_read_csv_with_newlines_in_fields(self, tmp_path: Path) -> None:
        """Test reading CSV with newlines within quoted fields."""
        # Create CSV with multiline fields
        csv_file = tmp_path / "multiline.csv"
        csv_file.write_text('name,description\nItem A,"Line 1\nLine 2"\n')

        # Read the CSV
        result = csv_read(csv_file)

        assert len(result) == 1
        assert result[0]["description"] == "Line 1\nLine 2"

    def test_read_nonexistent_file_raises_error(self, tmp_path: Path) -> None:
        """Test that reading nonexistent file raises FileNotFoundError."""
        csv_file = tmp_path / "nonexistent.csv"

        with pytest.raises(FileNotFoundError):
            csv_read(csv_file)

    def test_read_csv_preserves_column_order(self, tmp_path: Path) -> None:
        """Test that column order is preserved from first row."""
        # Create CSV
        csv_file = tmp_path / "order.csv"
        csv_file.write_text("z_col,a_col,m_col\nval1,val2,val3\n")

        # Read the CSV
        result = csv_read(csv_file)

        # Keys should match the order in the file
        assert list(result[0].keys()) == ["z_col", "a_col", "m_col"]

    @pytest.mark.parametrize(
        "delimiter,content",
        [
            (",", "a,b\n1,2\n"),
            ("|", "a|b\n1|2\n"),
            (";", "a;b\n1;2\n"),
        ],
    )
    def test_read_various_delimiters(
        self, tmp_path: Path, delimiter: str, content: str
    ) -> None:
        """Test reading CSVs with various delimiters."""
        csv_file = tmp_path / "delim.csv"
        csv_file.write_text(content)

        result = csv_read(csv_file, delimiter=delimiter)

        assert len(result) == 1
        assert result[0] == {"a": "1", "b": "2"}
