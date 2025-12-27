from __future__ import annotations

import gzip
import io

from rite.filesystem.compress.file_gzip_uncompress import uncompress_file


def test_uncompress_file_roundtrip() -> None:
    original_data = b"hello gzip"
    buffer = io.BytesIO()
    with gzip.GzipFile(fileobj=buffer, mode="wb") as gz:
        gz.write(original_data)
    buffer.seek(0)

    uncompressed, new_name = uncompress_file(buffer, filename="example.txt.gz")
    try:
        assert new_name == "example.txt"
        assert uncompressed.read() == original_data
    finally:
        uncompressed.close()
