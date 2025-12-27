from __future__ import annotations

import io

from rite.filesystem import file_size_to_string


def test_file_size_to_string_from_stream_units() -> None:
    buffer = io.BytesIO(b"1234567890")  # 10 bytes
    size_string = file_size_to_string(buffer)
    assert any(unit in size_string for unit in ("B", "KB", "MB"))
