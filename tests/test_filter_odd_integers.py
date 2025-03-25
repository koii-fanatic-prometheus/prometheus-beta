import pytest
from src.filter_odd_integers import filter_and_sort_odd_integers

def test_filter_and_sort_odd_integers_basic():
    """Test filtering and sorting odd integers from a mixed list."""
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert filter_and_sort_odd_integers(input_list) == [1, 3, 5, 7, 9]

def test_filter_and_sort_odd_integers_no_odds():
    """Test when no odd integers are present."""
    input_list = [2, 4, 6, 8]
    assert filter_and_sort_odd_integers(input_list) == []

def test_filter_and_sort_odd_integers_empty_list():
    """Test with an empty list."""
    input_list = []
    assert filter_and_sort_odd_integers(input_list) == []

def test_filter_and_sort_odd_integers_negative_numbers():
    """Test with negative odd and even integers."""
    input_list = [-1, -2, -3, -4, -5, 0, 1, 2, 3]
    assert filter_and_sort_odd_integers(input_list) == [-5, -3, -1, 1, 3]

def test_filter_and_sort_odd_integers_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_and_sort_odd_integers("not a list")

def test_filter_and_sort_odd_integers_invalid_element_type():
    """Test raising TypeError for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        filter_and_sort_odd_integers([1, 2, "3", 4, 5])