import pytest
from src.max_subarray_sum import max_subarray_sum

def test_normal_array():
    """Test with a typical array containing positive and negative numbers"""
    assert max_subarray_sum([1, -2, 3, 4, -1, 5]) == 11

def test_all_negative_array():
    """Test with an array of all negative numbers"""
    assert max_subarray_sum([-1, -2, -3, -4]) == -1

def test_all_positive_array():
    """Test with an array of all positive numbers"""
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15

def test_single_element_array():
    """Test with a single element array"""
    assert max_subarray_sum([42]) == 42

def test_alternating_array():
    """Test with an alternating array of positive and negative numbers"""
    assert max_subarray_sum([-1, 2, -3, 4, -5]) == 4

def test_invalid_input_type():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        max_subarray_sum("not a list")
    with pytest.raises(TypeError):
        max_subarray_sum(123)

def test_empty_list():
    """Test that ValueError is raised for an empty list"""
    with pytest.raises(ValueError):
        max_subarray_sum([])