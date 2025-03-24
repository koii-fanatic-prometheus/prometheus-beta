import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from heap_sort import heap_sort

def test_heap_sort_basic():
    """Test heap sort with a basic unsorted list."""
    input_list = [4, 1, 3, 9, 7]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_already_sorted():
    """Test heap sort with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    expected = input_list.copy()
    assert heap_sort(input_list) == expected

def test_heap_sort_reverse_sorted():
    """Test heap sort with a reverse sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_duplicates():
    """Test heap sort with a list containing duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_empty_list():
    """Test heap sort with an empty list."""
    input_list = []
    expected = []
    assert heap_sort(input_list) == expected

def test_heap_sort_single_element():
    """Test heap sort with a single-element list."""
    input_list = [42]
    expected = [42]
    assert heap_sort(input_list) == expected

def test_heap_sort_negative_numbers():
    """Test heap sort with negative numbers."""
    input_list = [-4, 1, -9, 0, 5, -2]
    expected = sorted(input_list)
    assert heap_sort(input_list) == expected

def test_heap_sort_non_list_input():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        heap_sort("not a list")
    
    with pytest.raises(TypeError):
        heap_sort(123)

def test_heap_sort_original_list_unchanged():
    """Test that the original list remains unchanged."""
    input_list = [4, 1, 3, 9, 7]
    original_copy = input_list.copy()
    heap_sort(input_list)
    assert input_list == original_copy