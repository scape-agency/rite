# Import | Future
from __future__ import annotations

# Import | Standard Library
import io

# Import | Local Modules
from rite.filesystem.compress.file_gzip_compress import compress_file


def test_compress_file_creates_gzip_and_suffix() -> None:
    source = io.BytesIO(b"hello world")
    compressed, new_name = compress_file(source, filename="example.txt")
    try:
        assert new_name.endswith(".gz")
        compressed.seek(0)
        # gzip header always starts with 0x1f 0x8b
        assert compressed.read(2) == b"\x1f\x8b"
    finally:
        compressed.close()
