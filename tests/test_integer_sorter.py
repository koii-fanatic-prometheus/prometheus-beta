import pytest
from src.integer_sorter import merge_sort

def test_empty_list():
    """Test sorting an empty list."""
    assert merge_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element."""
    assert merge_sort([42]) == [42]

def test_already_sorted_list():
    """Test sorting a list that is already sorted."""
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted_list():
    """Test sorting a list in reverse order."""
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements."""
    assert merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]

def test_negative_and_positive_numbers():
    """Test sorting a list with negative and positive numbers."""
    assert merge_sort([-5, 2, 0, -3, 7, 1]) == [-5, -3, 0, 1, 2, 7]

def test_large_list():
    """Test sorting a larger list."""
    large_list = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    assert merge_sort(large_list) == sorted(large_list)

def test_invalid_input_type():
    """Test that a TypeError is raised when input is not a list."""
    with pytest.raises(TypeError, match="Input must be a list"):
        merge_sort("not a list")

def test_list_with_non_integer_elements():
    """Test that a TypeError is raised when list contains non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        merge_sort([1, 2, "three", 4])

def test_list_with_floating_point_numbers():
    """Test that a TypeError is raised when list contains floating point numbers."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        merge_sort([1.5, 2, 3, 4])