import pytest
from src.merge_sort import merge_sort

def test_merge_sort_basic_integers():
    """Test merge sort with a basic list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert merge_sort(arr) == expected

def test_merge_sort_empty_list():
    """Test merge sort with an empty list."""
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    """Test merge sort with a single-element list."""
    arr = [42]
    assert merge_sort(arr) == [42]

def test_merge_sort_already_sorted():
    """Test merge sort with an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == [1, 2, 3, 4, 5]

def test_merge_sort_reverse_sorted():
    """Test merge sort with a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert merge_sort(arr) == expected

def test_merge_sort_duplicate_elements():
    """Test merge sort with duplicate elements."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    expected = [1, 2, 2, 3, 3, 4, 8]
    assert merge_sort(arr) == expected

def test_merge_sort_floating_points():
    """Test merge sort with floating-point numbers."""
    arr = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert merge_sort(arr) == expected

def test_merge_sort_invalid_input():
    """Test merge sort with invalid input type."""
    with pytest.raises(TypeError):
        merge_sort("not a list")

def test_merge_sort_non_comparable_elements():
    """Test merge sort with non-comparable elements."""
    with pytest.raises(TypeError):
        merge_sort([1, 2, "3", {4}])