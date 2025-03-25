import pytest
from src.find_common import find_common

def test_find_common_basic():
    """Test finding common elements in simple lists"""
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    assert find_common(list1, list2) == [4, 5]

def test_find_common_empty_lists():
    """Test when both lists are empty"""
    assert find_common([], []) == []

def test_find_common_no_overlap():
    """Test when there are no common elements"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    assert find_common(list1, list2) == []

def test_find_common_duplicate_elements():
    """Test with lists containing duplicate elements"""
    list1 = [1, 2, 2, 3, 4, 4]
    list2 = [2, 4, 5, 6]
    assert find_common(list1, list2) == [2, 2, 4, 4]

def test_find_common_preserve_order():
    """Test that common elements preserve order of first list"""
    list1 = [5, 3, 1, 2, 4]
    list2 = [2, 4, 6, 1]
    assert find_common(list1, list2) == [1, 2, 4]

def test_find_common_mixed_types():
    """Test with lists of mixed hashable types"""
    list1 = [1, 'a', 2, 'b', 3]
    list2 = ['a', 1, 'c', 2]
    assert find_common(list1, list2) == [1, 'a', 2]

def test_find_common_case_sensitive():
    """Test case sensitivity for string elements"""
    list1 = ['Apple', 'Banana', 'Cherry']
    list2 = ['apple', 'banana', 'BANANA']
    assert find_common(list1, list2) == []