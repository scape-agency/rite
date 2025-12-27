# -*- coding: utf-8 -*-

"""Tests for Trie."""

from src.rite.collections.tree import Trie


class TestTrie:
    """Test cases for Trie class."""

    def test_init(self):
        """Test trie initialization."""
        trie = Trie()
        assert not trie.search("")
        assert len(trie) == 0

    def test_insert_single_word(self):
        """Test inserting a single word."""
        trie = Trie()
        trie.insert("hello")
        assert trie.search("hello")
        assert len(trie) == 1

    def test_insert_multiple_words(self):
        """Test inserting multiple words."""
        trie = Trie()
        words = ["hello", "world", "help", "hero"]
        for word in words:
            trie.insert(word)

        for word in words:
            assert trie.search(word)
        assert len(trie) == 4

    def test_insert_empty_string(self):
        """Test inserting empty string."""
        trie = Trie()
        trie.insert("")
        # Empty string should not be searchable
        assert not trie.search("")

    def test_search_nonexistent(self):
        """Test searching for non-existent word."""
        trie = Trie()
        trie.insert("hello")
        assert not trie.search("hell")
        assert not trie.search("helloo")
        assert not trie.search("world")

    def test_starts_with(self):
        """Test prefix checking."""
        trie = Trie()
        trie.insert("hello")
        trie.insert("help")

        assert trie.starts_with("hel")
        assert trie.starts_with("hello")
        assert trie.starts_with("he")
        assert not trie.starts_with("world")

    def test_delete_existing_word(self):
        """Test deleting existing word."""
        trie = Trie()
        trie.insert("hello")
        trie.insert("help")

        assert trie.delete("hello")
        assert not trie.search("hello")
        assert trie.search("help")
        assert len(trie) == 1

    def test_delete_nonexistent_word(self):
        """Test deleting non-existent word."""
        trie = Trie()
        trie.insert("hello")

        assert not trie.delete("world")
        assert len(trie) == 1

    def test_delete_empty_trie(self):
        """Test deleting from empty trie."""
        trie = Trie()
        assert not trie.delete("hello")

    def test_delete_prefix(self):
        """Test deleting a prefix doesn't affect longer words."""
        trie = Trie()
        trie.insert("hello")
        trie.insert("helloworld")

        trie.delete("hello")
        assert not trie.search("hello")
        assert trie.search("helloworld")

    def test_get_words_with_prefix(self):
        """Test getting all words with prefix."""
        trie = Trie()
        words = ["hello", "help", "hero", "world", "won"]
        for word in words:
            trie.insert(word)

        he_words = trie.get_words_with_prefix("he")
        assert set(he_words) == {"hello", "help", "hero"}

        wo_words = trie.get_words_with_prefix("wo")
        assert set(wo_words) == {"world", "won"}

    def test_get_words_no_prefix(self):
        """Test getting words with non-existent prefix."""
        trie = Trie()
        trie.insert("hello")

        words = trie.get_words_with_prefix("xyz")
        assert not words

    def test_autocomplete(self):
        """Test autocomplete functionality."""
        trie = Trie()
        words = ["python", "programming", "program", "product", "produce"]
        for word in words:
            trie.insert(word)

        completions = trie.autocomplete("pro")
        assert set(completions) == {
            "programming",
            "program",
            "product",
            "produce",
        }

        py_completions = trie.autocomplete("py")
        assert py_completions == ["python"]

    def test_autocomplete_no_results(self):
        """Test autocomplete with no matches."""
        trie = Trie()
        trie.insert("hello")

        completions = trie.autocomplete("world")
        assert not completions

    def test_len(self):
        """Test word count."""
        trie = Trie()
        assert len(trie) == 0

        trie.insert("hello")
        assert len(trie) == 1

        trie.insert("world")
        assert len(trie) == 2

        trie.delete("hello")
        assert len(trie) == 1

    def test_case_sensitivity(self):
        """Test case sensitivity."""
        trie = Trie()
        trie.insert("Hello")
        trie.insert("hello")

        # Should be case-sensitive
        assert trie.search("Hello")
        assert trie.search("hello")
        assert len(trie) == 2

    def test_repr(self):
        """Test string representation."""
        trie = Trie()
        trie.insert("hello")
        trie.insert("world")

        repr_str = repr(trie)
        assert "Trie" in repr_str
        assert "words=2" in repr_str
