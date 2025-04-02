import pytest
from src.max_subarray_sum import max_subarray_sum

def test_max_subarray_sum_standard_case():
    """Test a standard case with mixed positive and negative numbers."""
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray_sum(arr) == [4, -1, 2, 1]

def test_max_subarray_sum_all_positive():
    """Test an array with all positive numbers."""
    arr = [1, 2, 3, 4, 5]
    assert max_subarray_sum(arr) == [1, 2, 3, 4, 5]

def test_max_subarray_sum_all_negative():
    """Test an array with all negative numbers."""
    arr = [-1, -2, -3, -4, -5]
    assert max_subarray_sum(arr) == [-1]

def test_max_subarray_sum_single_element():
    """Test an array with a single element."""
    arr = [42]
    assert max_subarray_sum(arr) == [42]

def test_max_subarray_sum_empty_array():
    """Test an empty array."""
    arr = []
    assert max_subarray_sum(arr) == []

def test_max_subarray_sum_zero_elements():
    """Test an array with multiple zero elements."""
    arr = [0, 0, 0, 0]
    assert max_subarray_sum(arr) == [0]

def test_max_subarray_sum_mixed_zeros():
    """Test an array with mixed zeros and other numbers."""
    arr = [-1, 0, -2, 3, 0, 4, -5]
    assert max_subarray_sum(arr) == [3, 0, 4]