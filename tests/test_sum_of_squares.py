import pytest
from src.sum_of_squares import calculate_sum_of_squares

def test_sum_of_squares_positive_numbers():
    """Test sum of squares with positive numbers."""
    assert calculate_sum_of_squares([1, 2, 3]) == 14  # 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = 14

def test_sum_of_squares_mixed_numbers():
    """Test sum of squares with mixed positive and negative numbers."""
    assert calculate_sum_of_squares([-1, 0, 1]) == 2  # (-1)^2 + 0^2 + 1^2 = 1 + 0 + 1 = 2

def test_sum_of_squares_float_numbers():
    """Test sum of squares with floating-point numbers."""
    assert calculate_sum_of_squares([1.5, 2.5]) == pytest.approx(8.5)  # 1.5^2 + 2.5^2 = 2.25 + 6.25 = 8.5

def test_sum_of_squares_empty_list():
    """Test sum of squares with an empty list."""
    assert calculate_sum_of_squares([]) == 0

def test_sum_of_squares_invalid_input_type():
    """Test function raises TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        calculate_sum_of_squares("not a list")

def test_sum_of_squares_invalid_element_type():
    """Test function raises TypeError for list with non-numeric elements."""
    with pytest.raises(TypeError, match="All elements must be numbers"):
        calculate_sum_of_squares([1, 2, "three"])