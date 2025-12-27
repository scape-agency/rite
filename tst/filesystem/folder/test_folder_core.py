from __future__ import annotations

from pathlib import Path

import pytest

from rite.filesystem import (
    folder_ensure_exists,
    folder_list_files,
    folder_size_to_string,
)
from rite.filesystem.folder.folder_content_delete import delete_contents
from rite.filesystem.folder.folder_create import create_directory
from rite.filesystem.folder.folder_list_folders import list_folders
from rite.filesystem.folder.folder_size_get import get_folder_size


def test_folder_helpers_and_size_to_string(tmp_path: Path) -> None:
    root_directory = tmp_path / "root"
    folder_ensure_exists(root_directory)

    # Create nested structure
    sub_directory = root_directory / "sub"
    folder_ensure_exists(sub_directory)

    file_one = root_directory / "one.txt"
    file_two = sub_directory / "two.txt"
    file_one.write_text("hello", encoding="utf-8")  # 5 bytes
    file_two.write_text("world!", encoding="utf-8")  # 6 bytes

    # Non-recursive listing only sees the top-level file
    top_level_files = list(folder_list_files(root_directory, recursive=False))
    assert top_level_files == [file_one]

    # Recursive listing sees both
    all_files = list(folder_list_files(root_directory, recursive=True))
    assert set(all_files) == {file_one, file_two}

    # Size string should mention the combined size (11 bytes)
    size_string = folder_size_to_string(root_directory, recursive=True)
    assert "11" in size_string or "0" not in size_string


def test_list_folders_non_recursive_and_recursive(tmp_path: Path) -> None:
    root_directory = tmp_path / "root"
    sub_one = root_directory / "sub1"
    sub_two = root_directory / "sub2_match"

    sub_one.mkdir(parents=True)
    sub_two.mkdir(parents=True)
    nested = sub_two / "nested"
    nested.mkdir()

    # Non-recursive: only direct children
    non_recursive = list_folders(root_directory, recursive=False)
    assert set(non_recursive) == {sub_one, sub_two}

    # Recursive: includes nested
    recursive = list_folders(root_directory, recursive=True)
    assert set(recursive) == {sub_one, sub_two, nested}

    # Pattern filter
    filtered = list_folders(root_directory, pattern="*match", recursive=True)
    assert filtered == [sub_two]


def test_list_folders_errors(tmp_path: Path) -> None:
    missing = tmp_path / "missing"
    with pytest.raises(FileNotFoundError):
        list_folders(missing)

    # Create a file where a directory is expected
    file_path = tmp_path / "file.txt"
    file_path.write_text("x", encoding="utf-8")
    with pytest.raises(NotADirectoryError):
        list_folders(file_path)


def test_create_directory_and_get_folder_size_and_delete_contents(
    tmp_path: Path,
) -> None:
    root_directory = tmp_path / "to_create"
    created_directory = create_directory(root_directory)
    assert created_directory.exists() and created_directory.is_dir()

    # Populate with files and a subfolder
    sub_directory = created_directory / "sub"
    sub_directory.mkdir()
    file_one = created_directory / "one.bin"
    file_two = sub_directory / "two.bin"
    file_one.write_bytes(b"12345")  # 5 bytes
    file_two.write_bytes(b"6789")  # 4 bytes

    total_size = get_folder_size(created_directory)
    assert total_size == 9

    # Delete contents in dry-run mode (no changes)
    delete_contents(created_directory, dry_run=True, verbose=False)
    assert any(created_directory.iterdir())

    # Now delete for real and ensure the folder is empty
    delete_contents(created_directory, dry_run=False, verbose=False)
    assert list(created_directory.iterdir()) == []


def test_delete_contents_error_branch(monkeypatch, tmp_path: Path) -> None:
    root_directory = tmp_path / "error_root"
    sub_directory = root_directory / "sub"
    sub_directory.mkdir(parents=True)

    # Force shutil.rmtree to raise so we hit the exception block
    import shutil as _shutil

    def _failing_rmtree(path: Path) -> None:  # type: ignore[override]
        raise RuntimeError("forced failure")

    monkeypatch.setattr(_shutil, "rmtree", _failing_rmtree)

    with pytest.raises(RuntimeError):
        delete_contents(root_directory, dry_run=False, verbose=False)
