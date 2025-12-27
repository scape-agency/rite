from __future__ import annotations

from pathlib import Path

from rite.filesystem.folder.folder_size_to_string import folder_size_to_string


def test_folder_size_to_string_returns_human_readable(tmp_path: Path) -> None:
    root = tmp_path / "root"
    root.mkdir()
    (root / "a.bin").write_bytes(b"x" * 1024)

    size_str = folder_size_to_string(root, recursive=True)
    assert any(unit in size_str for unit in ("B", "KB", "MB"))
