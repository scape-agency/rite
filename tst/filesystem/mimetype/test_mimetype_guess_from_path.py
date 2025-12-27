from __future__ import annotations

from pathlib import Path

from rite.filesystem.mimetype.mimetype_guess_from_path import (
    mimetype_guess_from_path,
)


def test_mimetype_guess_from_path_with_extension(tmp_path: Path) -> None:
    path = tmp_path / "image.png"
    path.write_bytes(b"")

    mime, encoding = mimetype_guess_from_path(path)
    assert mime in {"image/png", "image/x-png"}
    assert encoding is None
