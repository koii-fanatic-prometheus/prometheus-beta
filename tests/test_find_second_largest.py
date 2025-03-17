import pytest
from src.find_second_largest import find_second_largest

def test_normal_array():
    """Test finding second largest in a normal array."""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4

def test_array_with_duplicates():
    """Test finding second largest with duplicate numbers."""
    assert find_second_largest([5, 5, 4, 3, 2]) == 4

def test_all_same_elements():
    """Test array with all identical elements."""
    assert find_second_largest([1, 1, 1]) is None

def test_two_element_array():
    """Test array with exactly two unique elements."""
    assert find_second_largest([1, 2]) == 1

def test_empty_array():
    """Test empty array returns None."""
    assert find_second_largest([]) is None

def test_single_element_array():
    """Test single element array returns None."""
    assert find_second_largest([42]) is None

def test_non_list_input():
    """Test that non-list input raises TypeError."""
    with pytest.raises(TypeError):
        find_second_largest("not a list")

def test_non_numeric_input():
    """Test that non-numeric elements raise ValueError."""
    with pytest.raises(ValueError):
        find_second_largest([1, 2, "three"])

def test_float_array():
    """Test array with floating point numbers."""
    assert find_second_largest([1.5, 2.7, 3.2, 0.5]) == 2.7

def test_mixed_numeric_types():
    """Test array with mixed integer and float types."""
    assert find_second_largest([1, 2.5, 3, 4.7]) == 3