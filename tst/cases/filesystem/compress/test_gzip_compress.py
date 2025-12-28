# =============================================================================
# Test: gzip_compress
# =============================================================================

"""
Tests for rite.filesystem.compress.gzip_compress.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Standard Library
import gzip
import io
import tempfile

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem.compress.gzip_compress import (
    compress_file,
)

# =============================================================================
# Test Functions
# =============================================================================


def test_compress_file() -> None:
    """Test compress_file() function with basic compression."""
    # Create a test file with content
    test_content = b"Hello, World! This is test content."
    input_file = io.BytesIO(test_content)

    # Compress the file
    output_file, new_filename = compress_file(input_file, "test.txt")

    # Verify the filename has .gz extension
    assert new_filename == "test.txt.gz"

    # Verify the output file is compressed
    output_file.seek(0)
    compressed_content = output_file.read()
    assert len(compressed_content) > 0

    # Verify we can decompress it back
    output_file.seek(0)
    with gzip.GzipFile(fileobj=output_file, mode="rb") as gz:
        decompressed = gz.read()
    assert decompressed == test_content

    output_file.close()


def test_compress_file_empty() -> None:
    """Test compress_file() with empty content."""
    input_file = io.BytesIO(b"")
    output_file, new_filename = compress_file(input_file, "empty.txt")

    assert new_filename == "empty.txt.gz"

    # Verify we can decompress empty file
    output_file.seek(0)
    with gzip.GzipFile(fileobj=output_file, mode="rb") as gz:
        decompressed = gz.read()
    assert decompressed == b""

    output_file.close()


def test_compress_file_large_content() -> None:
    """Test compress_file() with large content."""
    # Create large test content
    test_content = b"x" * 1000000  # 1MB of data
    input_file = io.BytesIO(test_content)

    output_file, new_filename = compress_file(input_file, "large.bin")

    assert new_filename == "large.bin.gz"

    # Verify compression worked
    output_file.seek(0)
    compressed_content = output_file.read()
    # Compressed content should be smaller than original
    assert len(compressed_content) < len(test_content)

    # Verify decompression
    output_file.seek(0)
    with gzip.GzipFile(fileobj=output_file, mode="rb") as gz:
        decompressed = gz.read()
    assert decompressed == test_content

    output_file.close()


def test_compress_file_filename_variations() -> None:
    """Test compress_file() with various filename formats."""
    test_content = b"test"
    test_cases = [
        ("file.txt", "file.txt.gz"),
        ("archive.tar", "archive.tar.gz"),
        ("no_extension", "no_extension.gz"),
        ("file.name.multiple.dots", "file.name.multiple.dots.gz"),
    ]

    for input_name, expected_name in test_cases:
        input_file = io.BytesIO(test_content)
        output_file, filename = compress_file(input_file, input_name)
        assert filename == expected_name
        output_file.close()
