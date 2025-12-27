from __future__ import annotations

from rite.filesystem.file.file_spooled_settings import (
    SpooledFileSettings,
    settings,
)


def test_spooled_file_settings_defaults() -> None:
    assert isinstance(settings, SpooledFileSettings)
    assert settings.TMP_FILE_MAX_SIZE > 0
    assert settings.TMP_FILE_READ_SIZE > 0
