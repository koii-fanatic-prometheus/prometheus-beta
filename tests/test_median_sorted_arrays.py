import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from median_sorted_arrays import find_median_sorted_arrays

def test_both_even_length_arrays():
    """Test median with two even-length arrays"""
    assert find_median_sorted_arrays([1, 3], [2, 4]) == 2.5

def test_both_odd_length_arrays():
    """Test median with two odd-length arrays"""
    assert find_median_sorted_arrays([1, 2], [3, 4, 5]) == 3

def test_one_empty_array():
    """Test when one array is empty"""
    assert find_median_sorted_arrays([], [1, 2, 3, 4, 5]) == 3

def test_different_sized_arrays():
    """Test arrays of different sizes"""
    assert find_median_sorted_arrays([1, 3, 5], [2, 4, 6, 8, 10]) == 4.5

def test_single_element_arrays():
    """Test arrays with single elements"""
    assert find_median_sorted_arrays([1], [2]) == 1.5

def test_large_arrays():
    """Test with larger arrays"""
    nums1 = [1, 3, 5, 7, 9]
    nums2 = [2, 4, 6, 8, 10, 12, 14]
    assert find_median_sorted_arrays(nums1, nums2) == 6.5

def test_float_arrays():
    """Test arrays with floating point numbers"""
    assert find_median_sorted_arrays([1.5, 2.5], [3.5, 4.5]) == 3

def test_negative_numbers():
    """Test arrays with negative numbers"""
    assert find_median_sorted_arrays([-5, -3, -1], [-2, 0, 2]) == -1.5

def test_type_error_non_list():
    """Test type error when non-list input is provided"""
    with pytest.raises(TypeError):
        find_median_sorted_arrays(1, [2, 3])

def test_value_error_non_numeric():
    """Test value error when non-numeric elements are present"""
    with pytest.raises(ValueError):
        find_median_sorted_arrays([1, 'a'], [2, 3])

def test_empty_arrays():
    """Test error when both arrays are empty"""
    with pytest.raises(ValueError):
        find_median_sorted_arrays([], [])