from __future__ import annotations

from pathlib import Path

from rite.filesystem.folder.folder_content_delete import delete_contents


def test_delete_contents_deletes_files_and_folders(tmp_path: Path) -> None:
    root = tmp_path / "root"
    (root / "sub").mkdir(parents=True)
    file1 = root / "file1.txt"
    file2 = root / "sub" / "file2.txt"
    file1.write_text("a")
    file2.write_text("b")

    delete_contents(root, dry_run=False, verbose=False)

    assert root.exists()
    assert not file1.exists()
    assert not (root / "sub").exists()


def test_delete_contents_raises_for_missing_or_non_dir(tmp_path: Path) -> None:
    missing = tmp_path / "missing"

    with __import__("pytest").raises(FileNotFoundError):
        delete_contents(missing)

    not_a_dir = tmp_path / "file.txt"
    not_a_dir.write_text("x")

    with __import__("pytest").raises(NotADirectoryError):
        delete_contents(not_a_dir)
