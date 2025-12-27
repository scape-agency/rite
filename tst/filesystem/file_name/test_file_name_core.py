from __future__ import annotations

from rite.filesystem.file_name.filename_sanitize import filename_sanitize
from rite.filesystem.file_name.filename_to_date import filename_to_date
from rite.filesystem.file_name.filename_to_datestring import (
    filename_to_datestring,
)


def test_filename_sanitize_basic_cases() -> None:
    assert filename_sanitize("my file (copy).txt") == "my_file__copy_.txt"
    assert (
        filename_sanitize("file:name?.txt", replacement="-")
        == "file-name-.txt"
    )

    long_name = "a" * 300
    sanitized = filename_sanitize(long_name, max_length=100)
    assert len(sanitized) == 100

    # All invalid characters -> fallback name
    assert filename_sanitize("!!!", replacement="_") == "___"


def test_filename_to_datestring_and_date() -> None:
    name = "backup-2024-12-31-235959.tar.gz"
    datestring = filename_to_datestring(name)
    assert datestring == "2024-12-31-235959"

    dt = filename_to_date(name)
    assert dt is not None
    assert dt.year == 2024
    assert dt.month == 12
    assert dt.day == 31

    assert filename_to_datestring("no-date-here.txt") is None
    assert filename_to_date("no-date-here.txt") is None
