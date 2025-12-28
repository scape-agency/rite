# =============================================================================
# Test: Set Symmetric Difference
# =============================================================================

"""Tests for rite.collections.set.set_symmetric_difference."""

# Import | Future
from __future__ import annotations

# Import | Libraries
import pytest

# Import | Local Modules
from rite.collections.set import set_symmetric_difference


class TestSetSymmetricDifference:
    """Tests for set_symmetric_difference function."""

    def test_basic_symmetric_difference(self) -> None:
        """Test basic symmetric difference."""
        result = set_symmetric_difference({1, 2, 3}, {2, 3, 4})
        assert result == {1, 4}

    def test_symmetric_difference_no_overlap(self) -> None:
        """Test symmetric difference with no overlap."""
        result = set_symmetric_difference({1, 2}, {3, 4})
        assert result == {1, 2, 3, 4}

    def test_symmetric_difference_complete_overlap(self) -> None:
        """Test symmetric difference with complete overlap."""
        result = set_symmetric_difference({1, 2, 3}, {1, 2, 3})
        assert result == set()

    def test_symmetric_difference_empty_sets(self) -> None:
        """Test symmetric difference with empty sets."""
        result = set_symmetric_difference(set(), set())
        assert result == set()

    def test_symmetric_difference_one_empty(self) -> None:
        """Test symmetric difference with one empty set."""
        result = set_symmetric_difference({1, 2, 3}, set())
        assert result == {1, 2, 3}

    def test_symmetric_difference_first_empty(self) -> None:
        """Test symmetric difference with first set empty."""
        result = set_symmetric_difference(set(), {1, 2, 3})
        assert result == {1, 2, 3}

    def test_symmetric_difference_single_common(self) -> None:
        """Test symmetric difference with single common element."""
        result = set_symmetric_difference({1, 2}, {2, 3})
        assert result == {1, 3}

    def test_symmetric_difference_string_elements(self) -> None:
        """Test symmetric difference with string elements."""
        result = set_symmetric_difference({"a", "b", "c"}, {"b", "c", "d"})
        assert result == {"a", "d"}

    def test_symmetric_difference_large_sets(self) -> None:
        """Test symmetric difference with large sets."""
        set1 = set(range(1000))
        set2 = set(range(500, 1500))
        result = set_symmetric_difference(set1, set2)
        assert result == set(range(500)) | set(range(1000, 1500))

    def test_symmetric_difference_commutative(self) -> None:
        """Test that symmetric difference is commutative."""
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        result1 = set_symmetric_difference(set1, set2)
        result2 = set_symmetric_difference(set2, set1)
        assert result1 == result2


class TestSetSymmetricDifferenceEdgeCases:
    """Edge case tests for set_symmetric_difference."""

    def test_symmetric_difference_zero_element(self) -> None:
        """Test symmetric difference including zero."""
        result = set_symmetric_difference({0, 1, 2}, {1, 2, 3})
        assert result == {0, 3}

    def test_symmetric_difference_single_elements(self) -> None:
        """Test symmetric difference with single element sets."""
        result = set_symmetric_difference({1}, {2})
        assert result == {1, 2}

    def test_symmetric_difference_same_set(self) -> None:
        """Test symmetric difference of set with itself."""
        result = set_symmetric_difference({1, 2, 3}, {1, 2, 3})
        assert result == set()
