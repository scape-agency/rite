# =============================================================================
# Docstring
# =============================================================================

"""
Emoji Converter
===============

Replace words with corresponding emojis.

"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# =============================================================================
# Functions
# =============================================================================


def to_emoji_case(text: str) -> str:
    """
    Replace certain words with corresponding emojis.

    Note: This is a limited implementation; only a few words are replaced.

    Args:
        text: The text to convert

    Returns:
        The text with words replaced by emojis

    Example:
        >>> to_emoji_case("I love my dog")
        'I ❤️ my 🐶'
    """
    emoji_dict = {
        "love": "❤️",
        "happy": "😊",
        "sad": "😢",
        "dog": "🐶",
        "cat": "🐱",
        "tree": "🌳",
    }
    return " ".join(emoji_dict.get(word, word) for word in text.split())


# =============================================================================
# Exports
# =============================================================================

__all__: list[str] = [
    "to_emoji_case",
]
