import pytest
from src.find_min_max_difference import find_min_max_difference

def test_basic_case():
    """Test with a simple comma-separated string of integers."""
    assert find_min_max_difference("1,5,3,9") == 8

def test_negative_numbers():
    """Test with a string containing negative numbers."""
    assert find_min_max_difference("-1,5,3,-9") == 14

def test_single_number():
    """Test with a single number in the string."""
    assert find_min_max_difference("42") == 0

def test_repeating_numbers():
    """Test with repeating numbers."""
    assert find_min_max_difference("7,7,7,7") == 0

def test_white_space_handling():
    """Test that white spaces are handled correctly."""
    assert find_min_max_difference(" 1 , 5 , 3 , 9 ") == 8

def test_empty_string_raises_error():
    """Test that an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Input string cannot be empty"):
        find_min_max_difference("")

def test_non_integer_raises_error():
    """Test that non-integer input raises a ValueError."""
    with pytest.raises(ValueError, match="Input must be a string of comma-separated integers"):
        find_min_max_difference("1,2,three,4")

def test_no_valid_integers_raises_error():
    """Test that a string with no valid integers raises a ValueError."""
    with pytest.raises(ValueError, match="No valid integers found in the input string"):
        find_min_max_difference(" , , ")