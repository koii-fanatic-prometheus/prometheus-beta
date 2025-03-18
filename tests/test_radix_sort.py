import pytest
from src.radix_sort import radix_sort

def test_radix_sort_basic():
    """Test basic sorting of non-negative integers"""
    assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]

def test_radix_sort_empty_list():
    """Test sorting an empty list"""
    assert radix_sort([]) == []

def test_radix_sort_single_element():
    """Test sorting a list with a single element"""
    assert radix_sort([42]) == [42]

def test_radix_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    assert radix_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_radix_sort_with_zeros():
    """Test sorting a list with zeros"""
    assert radix_sort([0, 0, 0, 5, 3, 1]) == [0, 0, 0, 1, 3, 5]

def test_radix_sort_large_numbers():
    """Test sorting with large numbers"""
    large_list = [1000000, 2, 10, 1000, 100000, 10000]
    assert radix_sort(large_list) == [2, 10, 1000, 10000, 100000, 1000000]

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        radix_sort("not a list")

def test_invalid_element_type():
    """Test raising ValueError for non-integer elements"""
    with pytest.raises(ValueError, match="All elements must be integers"):
        radix_sort([1, 2, "3", 4])

def test_negative_numbers():
    """Test raising ValueError for negative numbers"""
    with pytest.raises(ValueError, match="Radix sort only works with non-negative integers"):
        radix_sort([1, -2, 3, 4])