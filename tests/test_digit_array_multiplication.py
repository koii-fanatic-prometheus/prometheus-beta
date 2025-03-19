import pytest
from src.digit_array_multiplication import multiply_digit_arrays

def test_basic_multiplication():
    """Test basic multiplication of two digit arrays"""
    A = [1, 2, 3]  # 123
    B = [4, 5, 6]  # 456
    assert multiply_digit_arrays(A, B) == [5, 6, 0, 8, 8]

def test_multiplication_with_zeros():
    """Test multiplication involving zeros"""
    A = [0, 0, 5]  # 5
    B = [1, 2, 0]  # 120
    assert multiply_digit_arrays(A, B) == [6, 0, 0]

def test_single_digit_multiplication():
    """Test multiplication of single-digit arrays"""
    A = [7]
    B = [8]
    assert multiply_digit_arrays(A, B) == [5, 6]

def test_empty_array_raises_error():
    """Test that empty arrays raise a ValueError"""
    with pytest.raises(ValueError, match="Input arrays cannot be empty"):
        multiply_digit_arrays([], [1, 2, 3])

def test_different_length_arrays_raises_error():
    """Test that arrays of different lengths raise a ValueError"""
    with pytest.raises(ValueError, match="Input arrays must be of equal length"):
        multiply_digit_arrays([1, 2], [3, 4, 5])

def test_non_digit_input_raises_error():
    """Test that non-integer or out-of-range inputs raise a TypeError"""
    with pytest.raises(TypeError, match="All elements must be integers between 0 and 9"):
        multiply_digit_arrays([1, 2, 10], [3, 4, 5])

def test_large_number_multiplication():
    """Test multiplication of larger numbers"""
    A = [9, 9, 9]  # 999
    B = [9, 9, 9]  # 999
    assert multiply_digit_arrays(A, B) == [9, 9, 8, 0, 0, 1]