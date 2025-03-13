import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_basic_lis_length():
    """Test basic functionality for length of LIS"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    assert longest_increasing_subsequence(arr) == 6

def test_basic_lis_sequence():
    """Test basic functionality for actual LIS sequence"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    assert longest_increasing_subsequence(arr, return_sequence=True) == [10, 22, 33, 50, 60, 80]

def test_empty_list():
    """Test empty list input"""
    assert longest_increasing_subsequence([]) == 0
    assert longest_increasing_subsequence([], return_sequence=True) == []

def test_single_element_list():
    """Test list with a single element"""
    arr = [5]
    assert longest_increasing_subsequence(arr) == 1
    assert longest_increasing_subsequence(arr, return_sequence=True) == [5]

def test_decreasing_list():
    """Test a strictly decreasing list"""
    arr = [5, 4, 3, 2, 1]
    assert longest_increasing_subsequence(arr) == 1
    assert longest_increasing_subsequence(arr, return_sequence=True) == [5]

def test_all_same_elements():
    """Test list with all same elements"""
    arr = [2, 2, 2, 2, 2]
    assert longest_increasing_subsequence(arr) == 1
    assert longest_increasing_subsequence(arr, return_sequence=True) == [2]

def test_invalid_input_type():
    """Test non-list input raises TypeError"""
    with pytest.raises(TypeError):
        longest_increasing_subsequence(123)
    with pytest.raises(TypeError):
        longest_increasing_subsequence("not a list")

def test_multiple_lis():
    """Test case with multiple possible longest increasing subsequences"""
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    assert longest_increasing_subsequence(arr) == 6
    assert longest_increasing_subsequence(arr, return_sequence=True) in [
        [0, 2, 6, 9, 13, 15],
        [0, 2, 6, 10, 13, 15],
        [0, 4, 6, 9, 13, 15],
        [0, 4, 6, 10, 13, 15],
        [0, 2, 6, 9, 11, 15],
        [0, 2, 6, 10, 11, 15],
        [0, 4, 6, 9, 11, 15],
        [0, 4, 6, 10, 11, 15]
    ]