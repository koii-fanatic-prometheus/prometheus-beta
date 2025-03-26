import pytest
from src.exclusive_multiples import filter_exclusive_multiples

def test_basic_filtering():
    """Test basic filtering of exclusive multiples."""
    input_list = [1, 2, 3, 4, 5, 6, 9, 10, 12, 15, 18, 20]
    expected = [3, 5, 6, 10, 12, 18, 20]
    assert filter_exclusive_multiples(input_list) == expected

def test_empty_list():
    """Test filtering an empty list."""
    assert filter_exclusive_multiples([]) == []

def test_no_exclusive_multiples():
    """Test a list with no exclusive multiples."""
    input_list = [1, 2, 4, 7, 11, 13, 14]
    assert filter_exclusive_multiples(input_list) == []

def test_all_multiples():
    """Test a list with only multiples of 3 or 5."""
    input_list = [3, 5, 6, 9, 10, 12, 15, 18, 20]
    expected = [3, 5, 6, 10, 12, 18, 20]
    assert filter_exclusive_multiples(input_list) == expected

def test_negative_numbers():
    """Test filtering with negative numbers."""
    input_list = [-3, -5, -6, -9, -10, -12, -15, -18, -20]
    expected = [-3, -5, -6, -10, -12, -18, -20]
    assert filter_exclusive_multiples(input_list) == expected

def test_input_type_error():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_exclusive_multiples("not a list")

def test_non_integer_error():
    """Test that a TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        filter_exclusive_multiples([1, 2, 3, "4", 5])

def test_mixed_sign_multiples():
    """Test filtering with mixed positive and negative numbers."""
    input_list = [-9, -6, -3, 0, 3, 6, 9, 5, -5, 10, -10]
    expected = [-9, -6, -3, 5, 6, 10, -10]
    assert filter_exclusive_multiples(input_list) == expected