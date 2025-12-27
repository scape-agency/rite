# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Local Modules
from rite.filesystem import file_write_text, move_file


def test_move_file_moves_between_directories(tmp_path: Path) -> None:
    source_dir = tmp_path / "src"
    dest_dir = tmp_path / "dst"
    source_dir.mkdir()
    dest_dir.mkdir()

    file_path = source_dir / "file.txt"
    file_write_text(file_path, "data")

    move_file(str(source_dir), "file.txt", str(dest_dir))
    assert not file_path.exists()
    assert (dest_dir / "file.txt").exists()
