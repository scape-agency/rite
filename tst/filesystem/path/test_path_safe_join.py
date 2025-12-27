from __future__ import annotations

import pytest

from rite.filesystem import path_safe_join


def test_path_safe_join_stays_under_base() -> None:
    base_directory_path = "/var/data"
    relative_path = path_safe_join(base_directory_path, "uploads", "file.txt")
    assert relative_path == "var/data/uploads/file.txt"

    with pytest.raises(ValueError):
        path_safe_join(base_directory_path, "../etc/passwd")
