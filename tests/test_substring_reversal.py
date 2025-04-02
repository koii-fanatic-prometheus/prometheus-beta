import pytest
from src.substring_reversal import reverse_substring

def test_basic_substring_reversal():
    """Test basic substring reversal"""
    assert reverse_substring("hello world", 0, 5) == "olleh world"
    assert reverse_substring("hello world", 6, 11) == "hello dlrow"

def test_substring_in_middle():
    """Test reversing a substring in the middle of the string"""
    assert reverse_substring("python programming", 7, 12) == "python rgorpamming"

def test_single_character_substring():
    """Test reversing a single character substring"""
    assert reverse_substring("abcdef", 2, 3) == "abcdef"

def test_full_string_reversal():
    """Test reversing the entire string"""
    assert reverse_substring("hello", 0, 5) == "olleh"

def test_empty_string():
    """Test empty string input"""
    assert reverse_substring("", 0, 0) == ""

def test_invalid_start_index():
    """Test negative start index"""
    with pytest.raises(ValueError):
        reverse_substring("hello", -1, 3)

def test_invalid_end_index():
    """Test end index greater than string length"""
    with pytest.raises(ValueError):
        reverse_substring("hello", 0, 6)

def test_start_greater_than_end():
    """Test when start index is greater than end index"""
    with pytest.raises(ValueError):
        reverse_substring("hello", 3, 2)

def test_incorrect_input_types():
    """Test incorrect input types"""
    with pytest.raises(TypeError):
        reverse_substring(123, 0, 3)
    with pytest.raises(TypeError):
        reverse_substring("hello", "0", 3)
    with pytest.raises(TypeError):
        reverse_substring("hello", 0, "3")