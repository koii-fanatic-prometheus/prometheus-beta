import pytest
from src.subarray_product_sum import count_subarrays_less_than_k

def test_basic_case():
    """Test a basic scenario with simple numbers."""
    nums = [10, 5, 2, 6]
    k = 100
    assert count_subarrays_less_than_k(nums, k) == 8

def test_all_elements_less_than_k():
    """Test when all subarrays have product less than k."""
    nums = [1, 2, 3, 4]
    k = 100
    assert count_subarrays_less_than_k(nums, k) == 10

def test_no_valid_subarrays():
    """Test when no subarrays have product less than k."""
    nums = [10, 20, 30]
    k = 5
    assert count_subarrays_less_than_k(nums, k) == 0

def test_empty_array():
    """Test behavior with an empty array."""
    nums = []
    k = 10
    assert count_subarrays_less_than_k(nums, k) == 0

def test_single_element_array():
    """Test an array with a single element."""
    nums = [5]
    k = 10
    assert count_subarrays_less_than_k(nums, k) == 1

def test_single_element_not_less_than_k():
    """Test an array with a single element not less than k."""
    nums = [10]
    k = 5
    assert count_subarrays_less_than_k(nums, k) == 0

def test_invalid_k():
    """Test raising ValueError for invalid k."""
    nums = [1, 2, 3]
    with pytest.raises(ValueError, match="k must be a positive integer"):
        count_subarrays_less_than_k(nums, 0)
    
    with pytest.raises(ValueError, match="k must be a positive integer"):
        count_subarrays_less_than_k(nums, -1)
    
    with pytest.raises(ValueError, match="k must be a positive integer"):
        count_subarrays_less_than_k(nums, "not an integer")