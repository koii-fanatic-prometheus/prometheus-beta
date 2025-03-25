import pytest
import time
from src.sleep_sort import sleep_sort

def test_sleep_sort_basic():
    """Test basic sorting of positive numbers."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    result = sleep_sort(input_list)
    assert result == sorted(input_list)

def test_sleep_sort_floats():
    """Test sorting of floating-point numbers."""
    input_list = [3.14, 1.41, 2.71, 0.58]
    result = sleep_sort(input_list)
    assert result == sorted(input_list)

def test_sleep_sort_empty_list():
    """Test sorting an empty list."""
    assert sleep_sort([]) == []

def test_sleep_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    result = sleep_sort(input_list)
    assert result == input_list

def test_sleep_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    result = sleep_sort(input_list)
    assert result == input_list

def test_sleep_sort_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        sleep_sort("not a list")

def test_sleep_sort_non_numeric():
    """Test raising ValueError for non-numeric elements."""
    with pytest.raises(ValueError, match="All elements must be numeric"):
        sleep_sort([1, 2, "three", 4])

def test_sleep_sort_negative_numbers():
    """Test raising ValueError for negative numbers."""
    with pytest.raises(ValueError, match="Sleep sort does not work with negative numbers"):
        sleep_sort([3, -1, 4, 2])

def test_sleep_sort_performance():
    """Basic performance check to ensure sorting works within reasonable time."""
    input_list = [5, 2, 9, 1, 7]
    start_time = time.time()
    result = sleep_sort(input_list)
    end_time = time.time()
    
    # Ensure correct sorting
    assert result == sorted(input_list)
    
    # Ensure sorting doesn't take too long 
    # (should be roughly proportional to max number * 0.001)
    assert end_time - start_time < 0.1  # Generous timeout