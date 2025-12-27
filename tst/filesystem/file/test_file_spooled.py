from __future__ import annotations

import io
from pathlib import Path

from rite.filesystem import create_spooled_temporary_file


def test_create_spooled_temporary_file_from_path_and_fileobj(
    tmp_path: Path,
) -> None:
    data_path = tmp_path / "data.bin"
    data_path.write_bytes(b"0123456789")

    spooled_from_path = create_spooled_temporary_file(filepath=data_path)
    try:
        assert spooled_from_path.read() == b"0123456789"
    finally:
        spooled_from_path.close()

    buffer = io.BytesIO(b"abcdef")
    spooled_from_obj = create_spooled_temporary_file(fileobj=buffer)
    try:
        assert spooled_from_obj.read() == b"abcdef"
    finally:
        spooled_from_obj.close()
