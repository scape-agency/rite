# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.filesystem import EXTENSION_REGEX


def test_extension_regex_matches_common_extensions() -> None:
    assert EXTENSION_REGEX.match("jpg")
    assert EXTENSION_REGEX.match("tar.gz")
