# =============================================================================
# Test: csv_write
# =============================================================================

"""
Tests for rite.serialization.csv.csv_write.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import csv
from pathlib import Path

# Import | Libraries
import pytest

# Import | Local Modules
from rite.serialization.csv.csv_write import (
    csv_write,
)

# =============================================================================
# Test Classes
# =============================================================================


class TestCsvWrite:
    """Tests for csv_write()."""

    def test_write_basic_csv(self, tmp_path: Path) -> None:
        """Test writing a basic CSV file."""
        # Prepare test data
        data = [
            {"name": "Alice", "age": "30", "city": "NYC"},
            {"name": "Bob", "age": "25", "city": "LA"},
        ]
        csv_file = tmp_path / "output.csv"

        # Write the CSV
        csv_write(csv_file, data)

        # Verify file was created and contains correct data
        assert csv_file.exists()
        content = csv_file.read_text()
        assert "name,age,city" in content
        assert "Alice,30,NYC" in content
        assert "Bob,25,LA" in content

    def test_write_csv_with_string_path(self, tmp_path: Path) -> None:
        """Test writing CSV using string path."""
        # Prepare test data
        data = [{"id": "1", "value": "test"}]
        csv_file = tmp_path / "output.csv"

        # Write using string path
        csv_write(str(csv_file), data)

        assert csv_file.exists()
        assert "id,value" in csv_file.read_text()

    def test_write_csv_with_path_object(self, tmp_path: Path) -> None:
        """Test writing CSV using Path object."""
        # Prepare test data
        data = [{"id": "1", "value": "test"}]
        csv_file = tmp_path / "output.csv"

        # Write using Path object
        csv_write(csv_file, data)

        assert csv_file.exists()

    def test_write_csv_with_tab_delimiter(self, tmp_path: Path) -> None:
        """Test writing CSV with tab delimiter."""
        # Prepare test data
        data = [
            {"name": "Alice", "age": "30"},
            {"name": "Bob", "age": "25"},
        ]
        tsv_file = tmp_path / "output.tsv"

        # Write with tab delimiter
        csv_write(tsv_file, data, delimiter="\t")

        # Verify content
        content = tsv_file.read_text()
        assert "name\tage" in content
        assert "Alice\t30" in content

    def test_write_csv_with_semicolon_delimiter(self, tmp_path: Path) -> None:
        """Test writing CSV with semicolon delimiter."""
        # Prepare test data
        data = [{"a": "1", "b": "2"}]
        csv_file = tmp_path / "output.csv"

        # Write with semicolon delimiter
        csv_write(csv_file, data, delimiter=";")

        # Verify content
        content = csv_file.read_text()
        assert "a;b" in content
        assert "1;2" in content

    def test_write_empty_list_does_nothing(self, tmp_path: Path) -> None:
        """Test writing empty list creates no file."""
        csv_file = tmp_path / "empty.csv"

        # Write empty data
        csv_write(csv_file, [])

        # File should not be created
        assert not csv_file.exists()

    def test_write_creates_parent_directories(self, tmp_path: Path) -> None:
        """Test that parent directories are created if needed."""
        # Prepare test data
        data = [{"id": "1"}]
        csv_file = tmp_path / "nested" / "deep" / "output.csv"

        # Write the CSV
        csv_write(csv_file, data)

        # Verify file and directories were created
        assert csv_file.exists()
        assert csv_file.parent.exists()

    def test_write_csv_with_special_characters(self, tmp_path: Path) -> None:
        """Test writing CSV with special characters."""
        # Prepare test data with special chars
        data = [
            {"name": 'Item "A"', "description": "Contains, comma"},
            {"name": "Item B", "description": 'Contains "quotes"'},
        ]
        csv_file = tmp_path / "special.csv"

        # Write the CSV
        csv_write(csv_file, data)

        # Read back and verify
        content = csv_file.read_text()
        assert 'Item "A"' in content or '"Item ""A"""' in content
        assert "Contains, comma" in content or '"Contains, comma"' in content

    def test_write_csv_with_newlines_in_fields(self, tmp_path: Path) -> None:
        """Test writing CSV with newlines in field values."""
        # Prepare test data with newlines
        data = [
            {"name": "Item A", "description": "Line 1\nLine 2"},
        ]
        csv_file = tmp_path / "multiline.csv"

        # Write the CSV
        csv_write(csv_file, data)

        # Read back using csv module to verify proper quoting
        rows = []
        with csv_file.open("r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)

        assert len(rows) == 1
        assert rows[0]["description"] == "Line 1\nLine 2"

    def test_write_csv_with_unicode(self, tmp_path: Path) -> None:
        """Test writing CSV with Unicode characters."""
        # Prepare test data with Unicode
        data = [
            {"name": "Alice", "greeting": "Hello"},
            {"name": "Böb", "greeting": "Hallö"},
            {"name": "José", "greeting": "¡Hola!"},
        ]
        csv_file = tmp_path / "unicode.csv"

        # Write the CSV
        csv_write(csv_file, data)

        # Verify content
        content = csv_file.read_text(encoding="utf-8")
        assert "Böb" in content
        assert "¡Hola!" in content

    def test_write_csv_with_empty_values(self, tmp_path: Path) -> None:
        """Test writing CSV with empty field values."""
        # Prepare test data with empty fields
        data = [
            {"name": "Alice", "email": "alice@test.com", "phone": ""},
            {"name": "Bob", "email": "", "phone": "555-1234"},
        ]
        csv_file = tmp_path / "empty.csv"

        # Write the CSV
        csv_write(csv_file, data)

        # Read back and verify empty fields
        rows = []
        with csv_file.open("r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)

        assert rows[0]["phone"] == ""
        assert rows[1]["email"] == ""

    def test_write_csv_overwrites_existing_file(self, tmp_path: Path) -> None:
        """Test that writing overwrites existing file."""
        csv_file = tmp_path / "output.csv"

        # Write first data
        data1 = [{"id": "1", "name": "First"}]
        csv_write(csv_file, data1)
        content1 = csv_file.read_text()

        # Write second data (overwrites)
        data2 = [{"id": "2", "name": "Second"}]
        csv_write(csv_file, data2)
        content2 = csv_file.read_text()

        # Verify second write overwrote the file
        assert "First" not in content2
        assert "Second" in content2

    def test_write_csv_single_row(self, tmp_path: Path) -> None:
        """Test writing CSV with single row."""
        # Prepare test data
        data = [{"id": "1", "value": "single"}]
        csv_file = tmp_path / "single.csv"

        # Write the CSV
        csv_write(csv_file, data)

        # Read back and verify
        rows = []
        with csv_file.open("r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)

        assert len(rows) == 1
        assert rows[0] == {"id": "1", "value": "single"}

    def test_write_csv_many_columns(self, tmp_path: Path) -> None:
        """Test writing CSV with many columns."""
        # Prepare test data with many columns
        data = [{f"col{i}": f"val{i}" for i in range(20)}]
        csv_file = tmp_path / "many_cols.csv"

        # Write the CSV
        csv_write(csv_file, data)

        # Verify all columns are in header
        first_line = csv_file.read_text().split("\n")[0]
        assert "col0" in first_line
        assert "col19" in first_line

    def test_write_csv_preserves_key_order(self, tmp_path: Path) -> None:
        """Test that CSV columns follow order from first row keys."""
        # Prepare test data
        data = [{"z": "1", "a": "2", "m": "3"}]
        csv_file = tmp_path / "order.csv"

        # Write the CSV
        csv_write(csv_file, data)

        # Read first line (header)
        first_line = csv_file.read_text().split("\n")[0]
        # Should follow order from dict keys
        assert first_line.startswith("z,a,m")

    @pytest.mark.parametrize(
        "delimiter,data",
        [
            (",", [{"a": "1", "b": "2"}]),
            ("|", [{"a": "1", "b": "2"}]),
            (";", [{"a": "1", "b": "2"}]),
            ("\t", [{"a": "1", "b": "2"}]),
        ],
    )
    def test_write_various_delimiters(
        self, tmp_path: Path, delimiter: str, data: list
    ) -> None:
        """Test writing CSVs with various delimiters."""
        csv_file = tmp_path / "delim.csv"

        csv_write(csv_file, data, delimiter=delimiter)

        content = csv_file.read_text()
        assert delimiter in content

    def test_write_csv_newline_parameter(self, tmp_path: Path) -> None:
        """Test that CSV is written with proper newline handling."""
        # Prepare test data
        data = [
            {"name": "Alice"},
            {"name": "Bob"},
        ]
        csv_file = tmp_path / "output.csv"

        # Write the CSV
        csv_write(csv_file, data)

        # Verify file can be read properly
        rows = []
        with csv_file.open("r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                rows.append(row)

        assert len(rows) == 2
