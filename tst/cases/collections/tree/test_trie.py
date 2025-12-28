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

    def test_delete_non_word(self) -> None:
        """Test deleting a prefix that's not marked as end-of-word."""
        instance = Trie()
        instance.insert("python")

        # Try to delete a prefix that's not a complete word
        assert instance.delete("py") is False
        assert instance.search("python")  # Original still there

    def test_delete_partial_path(self) -> None:
        """Test deleting when part of the path doesn't exist."""
        instance = Trie()
        instance.insert("cat")

        # Try to delete a word with overlapping prefix
        assert instance.delete("car") is False
        assert instance.search("cat")  # Original still there

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

    def test_insert_empty_string(self) -> None:
        """Test inserting empty string (line 79)."""
        instance = Trie()
        instance.insert("")
        assert len(instance) == 0

    def test_delete_returns_true_with_children(self) -> None:
        """Test delete when word has children (line 152)."""
        instance = Trie()
        instance.insert("he")
        instance.insert("hello")

        # Delete "he" but "hello" still exists
        result = instance.delete("he")
        assert result is True
        assert not instance.search("he")
        assert instance.search("hello")

    def test_get_words_prefix_returns_empty(self) -> None:
        """Test get_words_with_prefix with non-existent prefix (line 159)."""
        instance = Trie()
        instance.insert("apple")
        result = instance.get_words_with_prefix("xyz")
        assert result == []

    def test_insert_duplicate_word(self) -> None:
        """Test inserting duplicate word skips size increment (line 79->81)."""
        instance = Trie()
        instance.insert("hello")
        assert len(instance) == 1
        # Inserting same word again should not increment size
        instance.insert("hello")
        assert len(instance) == 1
        # Update value on duplicate insert
        instance.insert("hello", value="world")
        assert instance.get("hello") == "world"
        assert len(instance) == 1

    def test_delete_single_word_removes_nodes(self) -> None:
        """Test deleting single word removes orphan nodes (lines 162-163)."""
        instance = Trie()
        instance.insert("xyz")
        assert instance.search("xyz")
        # Delete should remove all nodes since no shared prefix
        result = instance.delete("xyz")
        assert result is True
        assert not instance.search("xyz")
        assert len(instance) == 0
