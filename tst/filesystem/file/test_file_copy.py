# Import | Future
from __future__ import annotations

# Import | Standard Library
from pathlib import Path

# Import | Local Modules
from rite.filesystem import copy_file, file_write_text


def test_copy_file_copies_contents(tmp_path: Path) -> None:
    source = tmp_path / "source.txt"
    destination = tmp_path / "dest.txt"
    file_write_text(source, "content")

    copy_file(source, destination)
    assert destination.read_text(encoding="utf-8") == "content"
