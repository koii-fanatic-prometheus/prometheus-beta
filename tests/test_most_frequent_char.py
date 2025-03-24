import pytest
from src.most_frequent_char import find_most_frequent_char

def test_basic_most_frequent():
    """Test finding the most frequent character in a simple string."""
    assert find_most_frequent_char("hello") == "l"

def test_first_most_frequent_when_tie():
    """Test returning the first most frequent character when multiple have same frequency."""
    assert find_most_frequent_char("aabbc") == "a"

def test_empty_string():
    """Test handling of empty string."""
    assert find_most_frequent_char("") == ""

def test_single_character():
    """Test a string with a single character."""
    assert find_most_frequent_char("a") == "a"

def test_all_unique_characters():
    """Test a string where all characters appear once."""
    assert find_most_frequent_char("abcde") == "a"

def test_special_characters():
    """Test with special characters and spaces."""
    assert find_most_frequent_char("!!hello world!!") == "!"

def test_invalid_input_type():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError):
        find_most_frequent_char(12345)
    with pytest.raises(TypeError):
        find_most_frequent_char(None)

def test_case_sensitivity():
    """Test that the function is case-sensitive."""
    assert find_most_frequent_char("Hello") == "l"
    assert find_most_frequent_char("hEllo") == "h"