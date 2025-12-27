from __future__ import annotations

from pathlib import Path

from rite.filesystem import file_read_text, file_write_text


def test_file_read_text_roundtrip(tmp_path: Path) -> None:
    path = tmp_path / "data.txt"
    file_write_text(path, "payload", encoding="utf-8")
    assert file_read_text(path, encoding="utf-8") == "payload"
