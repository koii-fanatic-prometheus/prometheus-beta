import pytest
from src.product_of_other_elements import product_of_other_elements

def test_standard_list():
    """Test a standard list of positive integers"""
    assert product_of_other_elements([1, 2, 3, 4]) == [24, 12, 8, 6]

def test_with_zeros():
    """Test list with zeros"""
    assert product_of_other_elements([1, 0, 3, 4]) == [0, 12, 0, 0]

def test_multiple_zeros():
    """Test list with multiple zeros"""
    assert product_of_other_elements([0, 0, 3, 4]) == [0, 0, 0, 0]

def test_single_element_list():
    """Test single element list"""
    assert product_of_other_elements([5]) == [1]

def test_empty_list():
    """Test empty list"""
    assert product_of_other_elements([]) == []

def test_negative_numbers():
    """Test list with negative numbers"""
    assert product_of_other_elements([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

def test_float_numbers():
    """Test list with float numbers"""
    assert product_of_other_elements([1.5, 2.5, 3.5]) == [8.75, 5.25, 3.75]

def test_invalid_input_type():
    """Test invalid input type"""
    with pytest.raises(ValueError, match="Input must be a list"):
        product_of_other_elements("not a list")

def test_invalid_element_type():
    """Test list with non-numeric elements"""
    with pytest.raises(TypeError, match="All list elements must be numeric"):
        product_of_other_elements([1, 2, "three"])