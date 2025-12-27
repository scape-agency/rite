from __future__ import annotations

from pathlib import Path

from rite.filesystem.folder.folder_size_get import get_folder_size


def test_get_folder_size_counts_all_files(tmp_path: Path) -> None:
    root = tmp_path / "root"
    root.mkdir()
    (root / "a.txt").write_bytes(b"abc")
    (root / "sub").mkdir()
    (root / "sub" / "b.txt").write_bytes(b"12345")

    size = get_folder_size(root)
    assert size == 3 + 5
