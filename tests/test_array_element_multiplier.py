import pytest
from src.array_element_multiplier import multiply_array_elements

def test_multiply_numeric_arrays():
    """Test multiplication of numeric arrays"""
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]
    assert multiply_array_elements(arr1, arr2) == [4, 10, 18]

def test_multiply_string_arrays():
    """Test multiplication of string arrays by repeating"""
    arr1 = ['a', 'b', 'c']
    arr2 = [3, 2, 4]
    assert multiply_array_elements(arr1, arr2) == ['aaa', 'bb', 'cccc']

def test_multiply_mixed_numeric_types():
    """Test multiplication of mixed numeric types"""
    arr1 = [1, 2.5, 3]
    arr2 = [4, 2, 6.0]
    assert multiply_array_elements(arr1, arr2) == [4, 5.0, 18.0]

def test_empty_arrays():
    """Test multiplication of empty arrays"""
    assert multiply_array_elements([], []) == []

def test_unequal_length_arrays():
    """Test that an error is raised for arrays of different lengths"""
    with pytest.raises(ValueError, match="Input arrays must have the same length"):
        multiply_array_elements([1, 2], [1, 2, 3])

def test_unmultiplicable_types():
    """Test that an error is raised for types that cannot be multiplied"""
    with pytest.raises(TypeError):
        multiply_array_elements([1, 2], [1, "string"])

def test_none_values():
    """Test handling of None values"""
    with pytest.raises(TypeError):
        multiply_array_elements([1, None], [2, 3])