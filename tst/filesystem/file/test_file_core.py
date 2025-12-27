from __future__ import annotations

import io
from pathlib import Path
from typing import BinaryIO, cast

import pytest

from rite.filesystem import EXTENSION_REGEX  # kept here for now
from rite.filesystem import (
    compress_file,
    copy_file,
    copy_files,
    create_spooled_temporary_file,
    delete_file,
    extension_normalize,
    extension_validate,
    file_read_bytes,
    file_read_text,
    file_size_to_string,
    file_write_bytes,
    file_write_text,
    move_file,
    rename_file,
    uncompress_file,
)


def test_read_and_write_text_and_bytes(tmp_path: Path) -> None:
    file_path = tmp_path / "sample.txt"

    file_write_text(file_path, "hello", encoding="utf-8")
    assert file_read_text(file_path, encoding="utf-8") == "hello"

    binary_path = tmp_path / "sample.bin"
    file_write_bytes(binary_path, b"data")
    assert file_read_bytes(binary_path) == b"data"


def test_copy_files_non_recursive_and_recursive(tmp_path: Path) -> None:
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "nested"
    target_dir = tmp_path / "dst"

    nested_dir.mkdir(parents=True)
    (source_dir / "root.txt").write_text("root", encoding="utf-8")
    (nested_dir / "nested.txt").write_text("nested", encoding="utf-8")

    # Non-recursive: only top-level file is copied
    copy_files(source_dir, target_dir, recursive=False)
    assert (target_dir / "root.txt").exists()
    assert not (target_dir / "nested" / "nested.txt").exists()

    # Recursive: nested files are copied as well
    copy_files(source_dir, target_dir, recursive=True)
    assert (target_dir / "nested" / "nested.txt").exists()

    # Missing source directory raises FileNotFoundError
    with pytest.raises(FileNotFoundError):
        copy_files(tmp_path / "missing", target_dir)


def test_copy_move_rename_and_delete_file(tmp_path: Path) -> None:
    source_directory = tmp_path / "src"
    destination_directory = tmp_path / "dst"
    source_directory.mkdir()

    source_file = source_directory / "file.txt"
    file_write_text(source_file, "content")

    copied_file = destination_directory / "copied.txt"
    # copy_file works with Path objects
    copy_file(source_file, copied_file)
    assert copied_file.exists()

    # move_file uses directory and filename arguments
    moved_directory = tmp_path / "moved"
    move_file(str(destination_directory), "copied.txt", str(moved_directory))
    moved_file = moved_directory / "copied.txt"
    assert moved_file.exists()
    assert not copied_file.exists()

    # rename_file within a directory
    rename_file(str(moved_directory), "copied.txt", "renamed.txt")
    renamed_file = moved_directory / "renamed.txt"
    assert renamed_file.exists()

    # delete_file removes the file
    delete_file(str(moved_directory), "renamed.txt")
    assert not renamed_file.exists()

    # delete_file on a missing file raises FileNotFoundError
    with pytest.raises(FileNotFoundError):
        delete_file(str(moved_directory), "missing.txt")


def test_file_size_to_string_from_stream() -> None:
    buffer = io.BytesIO(b"1234567890")  # 10 bytes
    size_string = file_size_to_string(buffer)
    assert any(unit in size_string for unit in ("B", "KB", "MB"))


def test_create_spooled_temporary_file_from_path_and_fileobj(
    tmp_path: Path,
) -> None:
    # Seed from a real file path
    data_path = tmp_path / "data.bin"
    data_path.write_bytes(b"0123456789")

    spooled_from_path = create_spooled_temporary_file(filepath=data_path)
    try:
        assert spooled_from_path.read() == b"0123456789"
    finally:
        spooled_from_path.close()

    # Seed from an in-memory file-like object
    buffer = io.BytesIO(b"abcdef")
    spooled_from_obj = create_spooled_temporary_file(fileobj=buffer)
    try:
        assert spooled_from_obj.read() == b"abcdef"
    finally:
        spooled_from_obj.close()


def test_extension_normalize_and_validate() -> None:
    assert extension_normalize(".JPG") == "jpg"
    assert extension_normalize(" PDF ", leading_dot=True) == ".pdf"
    assert extension_normalize("   ") is None

    # Validation passes for allowed extensions
    extension_validate("jpg", allowed=["jpg", "png"])

    # Invalid extensions and disallowed values raise ValueError
    with pytest.raises(ValueError):
        extension_validate("!")

    with pytest.raises(ValueError):
        extension_validate("exe", allowed=["jpg", "png"])

    # Regex should match typical extensions
    assert EXTENSION_REGEX.match("jpg")
    assert EXTENSION_REGEX.match("tar.gz")


def test_compress_and_uncompress_round_trip(tmp_path: Path) -> None:
    original_content = b"compressed data payload"

    # Create a source file-like object
    source_file = io.BytesIO(original_content)

    compressed_file, compressed_name = compress_file(
        source_file,
        str(tmp_path / "data.bin"),
    )
    assert compressed_name.endswith(".gz")

    try:
        # Use the compressed spooled file as input for decompression
        uncompressed_file, uncompressed_name = uncompress_file(
            cast(BinaryIO, compressed_file),
            compressed_name,
        )
        assert uncompressed_name == "data.bin"

        # Read back the decompressed content
        uncompressed_file.seek(0)
        decompressed_content = uncompressed_file.read()
        assert decompressed_content == original_content
    finally:
        compressed_file.close()
        uncompressed_file.close()
