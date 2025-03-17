import pytest
from src.array_rotation import rotate_array_left

def test_basic_rotation():
    """Test basic left rotation"""
    assert rotate_array_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]

def test_full_rotation():
    """Test rotation equal to array length"""
    assert rotate_array_left([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

def test_zero_rotation():
    """Test zero rotation returns same array"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_left(arr, 0) == arr
    assert rotate_array_left(arr, 0) is not arr  # Should be a copy

def test_rotation_larger_than_array():
    """Test rotation larger than array length"""
    assert rotate_array_left([1, 2, 3, 4, 5], 7) == [3, 4, 5, 1, 2]

def test_empty_array():
    """Test rotation of empty array"""
    assert rotate_array_left([], 3) == []

def test_single_element_array():
    """Test rotation of single-element array"""
    assert rotate_array_left([42], 5) == [42]

def test_invalid_input_type():
    """Test invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)
    
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_left([1, 2, 3], "2")

def test_negative_array():
    """Test array with negative numbers"""
    assert rotate_array_left([-1, -2, -3, -4, -5], 2) == [-3, -4, -5, -1, -2]

def test_mixed_type_array():
    """Test array with mixed types"""
    arr = [1, "two", 3.0, [4], {"five": 5}]
    result = rotate_array_left(arr, 2)
    assert result == [3.0, [4], {"five": 5}, 1, "two"]