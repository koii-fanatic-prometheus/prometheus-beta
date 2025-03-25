import pytest
from src.max_subarray_sum import max_subarray_sum

def test_standard_positive_numbers():
    """Test with a mix of positive and negative numbers"""
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_all_positive_numbers():
    """Test when all numbers are positive"""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_all_negative_numbers():
    """Test when all numbers are negative"""
    assert max_subarray_sum([-1, -2, -3, -4, -5]) == -1

def test_single_element_positive():
    """Test with a single positive element"""
    assert max_subarray_sum([42]) == 42

def test_single_element_negative():
    """Test with a single negative element"""
    assert max_subarray_sum([-42]) == -42

def test_alternating_numbers():
    """Test with alternating positive and negative numbers"""
    assert max_subarray_sum([1, -1, 2, -2, 3, -3]) == 3

def test_invalid_input_empty_list():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        max_subarray_sum([])

def test_invalid_input_not_a_list():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list of integers"):
        max_subarray_sum("not a list")
        max_subarray_sum(123)
        max_subarray_sum(None)