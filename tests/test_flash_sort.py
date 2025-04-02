import pytest
import random
from src.flash_sort import flash_sort

def test_flash_sort_basic_list():
    """Test sorting a basic list of integers."""
    arr = [5, 2, 9, 1, 7, 6, 3]
    sorted_arr = sorted(arr)
    result = flash_sort(arr)
    assert result == sorted_arr
    assert arr == sorted_arr

def test_flash_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    result = flash_sort(arr)
    assert result == []

def test_flash_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    result = flash_sort(arr)
    assert result == [42]

def test_flash_sort_all_same_elements():
    """Test sorting a list with all identical elements."""
    arr = [7, 7, 7, 7, 7]
    result = flash_sort(arr)
    assert result == arr

def test_flash_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-5, -2, -9, -1, -7, -6, -3]
    sorted_arr = sorted(arr)
    result = flash_sort(arr)
    assert result == sorted_arr
    assert arr == sorted_arr

def test_flash_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers."""
    arr = [-5, 2, 0, 9, -1, 7, 6, -3]
    sorted_arr = sorted(arr)
    result = flash_sort(arr)
    assert result == sorted_arr
    assert arr == sorted_arr

def test_flash_sort_large_random_list():
    """Test sorting a large random list."""
    arr = [random.randint(-1000, 1000) for _ in range(1000)]
    sorted_arr = sorted(arr)
    result = flash_sort(arr)
    assert result == sorted_arr
    assert arr == sorted_arr

def test_flash_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = list(range(10))
    result = flash_sort(arr)
    assert result == arr

def test_flash_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = list(range(10, 0, -1))
    sorted_arr = sorted(arr)
    result = flash_sort(arr)
    assert result == sorted_arr
    assert arr == sorted_arr

def test_flash_sort_invalid_input():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        flash_sort("not a list")

def test_flash_sort_non_comparable():
    """Test that ValueError is raised for non-comparable elements."""
    with pytest.raises(ValueError):
        flash_sort([1, 2, [3], 4])

def test_flash_sort_float_values():
    """Test sorting a list of floating-point numbers."""
    arr = [5.5, 2.3, 9.1, 1.7, 6.2]
    sorted_arr = sorted(arr)
    result = flash_sort(arr)
    assert result == sorted_arr
    assert arr == sorted_arr