from __future__ import annotations

from pathlib import Path

from rite.filesystem.folder.folder_list_files import folder_list_files


def test_folder_list_files_non_recursive(tmp_path: Path) -> None:
    root = tmp_path / "root"
    root.mkdir()
    (root / "a.txt").write_text("a")
    (root / "b.txt").write_text("b")
    (root / "sub").mkdir()
    (root / "sub" / "c.txt").write_text("c")

    files = sorted(p.name for p in folder_list_files(root, recursive=False))
    assert files == ["a.txt", "b.txt"]


def test_folder_list_files_recursive(tmp_path: Path) -> None:
    root = tmp_path / "root"
    root.mkdir()
    (root / "a.txt").write_text("a")
    (root / "sub").mkdir()
    (root / "sub" / "b.txt").write_text("b")

    files = sorted(
        p.relative_to(root).as_posix()
        for p in folder_list_files(root, recursive=True)
    )
    assert files == ["a.txt", "sub/b.txt"]
