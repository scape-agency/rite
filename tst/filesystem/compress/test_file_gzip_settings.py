# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem.compress.file_gzip_settings import (
    GzipCompressionSettings,
    settings,
)


def test_gzip_settings_defaults() -> None:
    assert isinstance(settings, GzipCompressionSettings)
    assert settings.TMP_FILE_MAX_SIZE > 0
    assert settings.TMP_FILE_READ_SIZE > 0
