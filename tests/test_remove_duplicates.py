import pytest
from src.remove_duplicates import remove_duplicates_and_sort

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates and sorting"""
    input_arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 2, 3, 4, 5, 6, 9]
    assert remove_duplicates_and_sort(input_arr) == expected

def test_remove_duplicates_already_sorted():
    """Test when input is already sorted"""
    input_arr = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates_and_sort(input_arr) == expected

def test_remove_duplicates_reverse_sorted():
    """Test when input is reverse sorted"""
    input_arr = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert remove_duplicates_and_sort(input_arr) == expected

def test_remove_duplicates_all_duplicates():
    """Test when all elements are duplicates"""
    input_arr = [2, 2, 2, 2, 2]
    expected = [2]
    assert remove_duplicates_and_sort(input_arr) == expected

def test_remove_duplicates_empty_list():
    """Test with an empty list"""
    input_arr = []
    expected = []
    assert remove_duplicates_and_sort(input_arr) == expected

def test_remove_duplicates_single_element():
    """Test with a single element"""
    input_arr = [42]
    expected = [42]
    assert remove_duplicates_and_sort(input_arr) == expected

def test_invalid_input_non_list():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates_and_sort("not a list")

def test_invalid_input_non_integers():
    """Test raising TypeError for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        remove_duplicates_and_sort([1, 2, "3", 4])

def test_remove_duplicates_negative_numbers():
    """Test with negative numbers"""
    input_arr = [-3, 1, -3, 0, 4, 1, -1]
    expected = [-3, -1, 0, 1, 4]
    assert remove_duplicates_and_sort(input_arr) == expected