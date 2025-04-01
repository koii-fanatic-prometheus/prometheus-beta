import pytest
from src.array_rotation import rotate_array

def test_basic_rotation():
    """Test basic right rotation of an array"""
    assert rotate_array([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotation_full_length():
    """Test rotation equal to array length (should return original array)"""
    original = [1, 2, 3, 4, 5]
    assert rotate_array(original, 5) == original

def test_rotation_more_than_length():
    """Test rotation more than array length"""
    assert rotate_array([1, 2, 3, 4, 5], 7) == [4, 5, 1, 2, 3]

def test_empty_array():
    """Test rotation of an empty array"""
    assert rotate_array([], 3) == []

def test_single_element_array():
    """Test rotation of a single-element array"""
    assert rotate_array([42], 5) == [42]

def test_zero_rotation():
    """Test rotation by zero positions"""
    original = [1, 2, 3, 4, 5]
    assert rotate_array(original, 0) == original

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array("not a list", 2)
    
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array([1, 2, 3], "2")

def test_negative_rotation():
    """Test error handling for negative rotation"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array([1, 2, 3], -1)