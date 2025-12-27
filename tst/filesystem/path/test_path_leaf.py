# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem import path_leaf


def test_path_leaf_returns_final_component() -> None:
    assert path_leaf("/some/folder/file.txt") == "file.txt"
    assert path_leaf("Documents/project") == "project"
