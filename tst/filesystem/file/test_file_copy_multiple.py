from __future__ import annotations

from pathlib import Path

from rite.filesystem import copy_files, file_write_text


def test_copy_files_recursive_and_non_recursive(tmp_path: Path) -> None:
    source_dir = tmp_path / "src"
    nested_dir = source_dir / "nested"
    target_dir = tmp_path / "dst"

    nested_dir.mkdir(parents=True)
    file_write_text(source_dir / "root.txt", "root")
    file_write_text(nested_dir / "nested.txt", "nested")

    copy_files(source_dir, target_dir, recursive=False)
    assert (target_dir / "root.txt").exists()
    assert not (target_dir / "nested" / "nested.txt").exists()

    copy_files(source_dir, target_dir, recursive=True)
    assert (target_dir / "nested" / "nested.txt").exists()
