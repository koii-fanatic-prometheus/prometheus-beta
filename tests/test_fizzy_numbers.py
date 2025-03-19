import pytest
from src.fizzy_numbers import generate_fizzy_numbers

def test_generate_fizzy_numbers_basic():
    """Test basic fizzy number generation."""
    assert generate_fizzy_numbers(10) == [3, 6, 7, 9, 10]

def test_generate_fizzy_numbers_edge_cases():
    """Test edge cases for fizzy number generation."""
    # Test with 1
    assert generate_fizzy_numbers(1) == []
    
    # Test with a number containing multiple divisible numbers
    assert generate_fizzy_numbers(21) == [3, 6, 7, 9, 10, 12, 14, 15, 18, 20, 21]

def test_generate_fizzy_numbers_invalid_input():
    """Test error handling for invalid inputs."""
    # Test with non-integer
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_fizzy_numbers("not an int")
    
    # Test with negative number
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_fizzy_numbers(-5)
    
    # Test with zero
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        generate_fizzy_numbers(0)

def test_generate_fizzy_numbers_sorted():
    """Ensure the returned list is sorted."""
    result = generate_fizzy_numbers(20)
    assert result == sorted(result), "Result should be in sorted order"