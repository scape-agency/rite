# =============================================================================
# Test: gzip_uncompress
# =============================================================================

"""
Tests for rite.filesystem.compress.gzip_uncompress.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import gzip
import io

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.compress.gzip_uncompress import (
    uncompress_file,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_uncompress_file() -> None:
    """Test uncompress_file() function with basic decompression."""
    # Create a gzip-compressed file
    original_content = b"Hello, World! This is test content."
    compressed_buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=compressed_buffer, mode="wb") as gz:
        gz.write(original_content)

    # Prepare the compressed file for reading
    compressed_buffer.seek(0)

    # Decompress the file
    output_file, new_filename = uncompress_file(
        compressed_buffer, "test.txt.gz"
    )

    # Verify the filename has .gz removed
    assert new_filename == "test.txt"

    # Verify the decompressed content matches original
    output_file.seek(0)
    decompressed_content = output_file.read()
    assert decompressed_content == original_content

    output_file.close()


def test_uncompress_file_empty() -> None:
    """Test uncompress_file() with empty compressed file."""
    # Create an empty gzip file
    compressed_buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=compressed_buffer, mode="wb") as gz:
        gz.write(b"")

    compressed_buffer.seek(0)

    output_file, new_filename = uncompress_file(compressed_buffer, "empty.gz")

    assert new_filename == "empty"

    # Verify decompressed content is empty
    output_file.seek(0)
    content = output_file.read()
    assert content == b""

    output_file.close()


def test_uncompress_file_large_content() -> None:
    """Test uncompress_file() with large compressed content."""
    # Create a large gzip file
    original_content = b"x" * 1000000  # 1MB of data
    compressed_buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=compressed_buffer, mode="wb") as gz:
        gz.write(original_content)

    compressed_buffer.seek(0)

    output_file, new_filename = uncompress_file(
        compressed_buffer, "large.bin.gz"
    )

    assert new_filename == "large.bin"

    # Verify decompressed content
    output_file.seek(0)
    decompressed = output_file.read()
    assert decompressed == original_content

    output_file.close()


def test_uncompress_file_filename_variations() -> None:
    """Test uncompress_file() with various filename formats."""
    original_content = b"test data"
    test_cases = [
        ("file.txt.gz", "file.txt"),
        ("archive.tar.gz", "archive.tar"),
        ("no_extension.gz", "no_extension"),
        ("multiple.dots.tar.gz", "multiple.dots.tar"),
    ]

    for input_name, expected_name in test_cases:
        # Create compressed data
        compressed_buffer = io.BytesIO()
        with gzip.GzipFile(fileobj=compressed_buffer, mode="wb") as gz:
            gz.write(original_content)

        compressed_buffer.seek(0)
        output_file, filename = uncompress_file(compressed_buffer, input_name)
        assert filename == expected_name
        output_file.close()
