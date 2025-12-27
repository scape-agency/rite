# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Libraries
import pytest

# Import | Local Modules
from rite.filesystem import (
    path_clean,
    path_exists,
    path_is_dir,
    path_is_file,
    path_leaf,
    path_safe_join,
    path_secure,
)


def test_path_clean_normalizes_leading_and_trailing_slashes() -> None:
    assert path_clean("//a/b//") == "/a/b"
    assert path_clean("a/b") == "/a/b"
    assert path_clean("/a/b") == "/a/b"


def test_path_leaf_returns_final_component() -> None:
    assert path_leaf("/some/folder/file.txt") == "file.txt"
    assert path_leaf("Documents/project") == "project"


def test_path_exists_and_type_checks(tmp_path: Path) -> None:
    directory_path = tmp_path / "dir"
    directory_path.mkdir()
    file_path = directory_path / "file.txt"
    file_path.write_text("data", encoding="utf-8")

    assert path_exists(directory_path)
    assert path_is_dir(directory_path)
    assert not path_is_file(directory_path)

    assert path_exists(file_path)
    assert path_is_file(file_path)
    assert not path_is_dir(file_path)


def test_path_safe_join_stays_under_base() -> None:
    base_directory_path = "/var/data"
    relative_path = path_safe_join(base_directory_path, "uploads", "file.txt")
    assert relative_path == "var/data/uploads/file.txt"

    with pytest.raises(ValueError):
        path_safe_join(base_directory_path, "../etc/passwd")


def test_path_secure_uses_only_basename() -> None:
    secure_path = path_secure("/var/data", "../../../etc/passwd")
    assert secure_path.endswith("/passwd")
    assert "/.." not in secure_path
