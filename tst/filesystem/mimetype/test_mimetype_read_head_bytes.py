from __future__ import annotations

import io
from pathlib import Path

from rite.filesystem.mimetype.mimetype_read_head_bytes import read_head_bytes


def test_read_head_bytes_from_bytes_and_path(tmp_path: Path) -> None:
    assert read_head_bytes(b"abcdef", n=3) == b"abc"

    path = tmp_path / "data.bin"
    path.write_bytes(b"xyz123")
    assert read_head_bytes(path, n=4) == b"xyz1"


def test_read_head_bytes_from_stream_preserves_position() -> None:
    stream = io.BytesIO(b"abcdef")
    stream.read(2)
    head = read_head_bytes(stream, n=3)
    assert head == b"cde"
    assert stream.read() == b"f"
