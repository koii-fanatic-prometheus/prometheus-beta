import pytest
from src.unique_pairs import find_unique_pairs

def test_find_unique_pairs_basic():
    """Test basic functionality of finding unique pairs."""
    result = find_unique_pairs([1, 2, 3, 4])
    expected = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    assert sorted(result) == sorted(expected)

def test_find_unique_pairs_empty_list():
    """Test behavior with an empty list."""
    assert find_unique_pairs([]) == []

def test_find_unique_pairs_single_element():
    """Test behavior with a single element list."""
    assert find_unique_pairs([1]) == []

def test_find_unique_pairs_duplicate_elements():
    """Test behavior with duplicate elements."""
    result = find_unique_pairs([1, 1, 2, 2])
    expected = [(1, 2)]
    assert sorted(result) == sorted(expected)

def test_find_unique_pairs_negative_numbers():
    """Test functionality with negative numbers."""
    result = find_unique_pairs([-1, 0, 1])
    expected = [(-1, 0), (-1, 1), (0, 1)]
    assert sorted(result) == sorted(expected)

def test_find_unique_pairs_result_is_unique():
    """Ensure that each pair appears only once, regardless of order."""
    result = find_unique_pairs([1, 2, 3])
    # Check that no pair appears twice and order doesn't matter
    assert len(result) == len(set(tuple(sorted(pair)) for pair in result))