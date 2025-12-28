# =============================================================================
# Test: trie
# =============================================================================

"""
Tests for rite.collections.tree.trie.
"""

# =============================================================================
# Imports
# =============================================================================

# Import | Future
from __future__ import annotations

# Import | Local Modules
from rite.collections.tree.trie import (
    Trie,
    TrieNode,
)

# =============================================================================
# Test Class: TrieNode
# =============================================================================


class TestTrieNode:
    """Tests for TrieNode class."""

    def test_instantiation(self) -> None:
        """Test TrieNode can be instantiated."""
        # TODO: Implement test
        instance = TrieNode()
        assert instance is not None


# =============================================================================
# Test Class: Trie
# =============================================================================


class TestTrie:
    """Tests for Trie class."""

    def test_instantiation(self) -> None:
        """Test Trie can be instantiated."""
        instance = Trie()
        assert len(instance) == 0
        assert not instance.search("")

    def test_insert(self) -> None:
        """Test Trie.insert() method."""
        instance = Trie()
        instance.insert("hello")
        assert instance.search("hello")
        assert "hello" in instance
        assert len(instance) == 1

        # Inserting empty string should be a no-op
        instance.insert("")
        assert len(instance) == 1

    def test_search(self) -> None:
        """Test Trie.search() method."""
        instance = Trie()
        instance.insert("hello")

        assert instance.search("hello") is True
        assert instance.search("hell") is False
        assert instance.search("world") is False

    def test_starts_with(self) -> None:
        """Test Trie.starts_with() method."""
        instance = Trie()
        instance.insert("hello")
        instance.insert("help")

        assert instance.starts_with("he")
        assert instance.starts_with("hello")
        assert not instance.starts_with("world")

    def test_get(self) -> None:
        """Test Trie.get() method."""
        instance = Trie()
        instance.insert("hello", value=42)

        assert instance.get("hello") == 42
        assert instance.get("world") is None

    def test_delete(self) -> None:
        """Test Trie.delete() method."""
        instance = Trie()
        instance.insert("hello")
        instance.insert("helloworld")

        # Deleting prefix should not remove longer word
        assert instance.delete("hello") is True
        assert not instance.search("hello")
        assert instance.search("helloworld")
        assert len(instance) == 1

        # Deleting non-existent word returns False
        assert instance.delete("missing") is False

    def test_get_words_with_prefix(self) -> None:
        """Test Trie.get_words_with_prefix() method."""
        instance = Trie()
        words = ["hello", "help", "hero", "world"]
        for word in words:
            instance.insert(word)

        he_words = instance.get_words_with_prefix("he")
        assert set(he_words) == {"hello", "help", "hero"}

        assert instance.get_words_with_prefix("xyz") == []

    def test_autocomplete(self) -> None:
        """Test Trie.autocomplete() method."""
        instance = Trie()
        words = ["python", "program", "product"]
        for word in words:
            instance.insert(word)

        completions = instance.autocomplete("pro")
        assert set(completions) == {"program", "product"}

    def test_get_all_words(self) -> None:
        """Test Trie.get_all_words() method."""
        instance = Trie()
        words = ["a", "b", "abc"]
        for word in words:
            instance.insert(word)

        all_words = instance.get_all_words()
        assert set(all_words) == set(words)

        # __repr__ smoke test
        repr_str = repr(instance)
        assert "Trie" in repr_str
