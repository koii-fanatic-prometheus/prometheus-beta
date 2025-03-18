import pytest
from src.two_sum import find_two_sum

def test_two_sum_basic_positive():
    """Test basic positive scenario"""
    assert find_two_sum([1, 2, 3, 4, 5], 7) == True

def test_two_sum_basic_negative():
    """Test basic negative scenario"""
    assert find_two_sum([1, 2, 3, 4, 5], 20) == False

def test_two_sum_edge_zero_target():
    """Test with zero as target"""
    assert find_two_sum([-1, 1, 2, 3], 0) == True

def test_two_sum_negative_numbers():
    """Test with negative numbers"""
    assert find_two_sum([-5, -2, 0, 2, 5], 0) == True

def test_two_sum_empty_list():
    """Test with empty list"""
    assert find_two_sum([], 5) == False

def test_two_sum_single_element():
    """Test with single element list"""
    assert find_two_sum([5], 10) == False

def test_two_sum_type_error_non_list():
    """Test type error for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_two_sum(123, 5)

def test_two_sum_type_error_non_integers():
    """Test type error for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_two_sum([1, 2, '3'], 5)

def test_two_sum_value_error_duplicates():
    """Test value error for duplicate numbers"""
    with pytest.raises(ValueError, match="Input list must contain unique integers"):
        find_two_sum([1, 2, 2, 3], 5)