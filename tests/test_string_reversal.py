import pytest
from src.string_reversal import reverse_string_in_place

def test_reverse_normal_string():
    """Test reversing a normal string"""
    s = list('hello')
    reverse_string_in_place(s)
    assert s == list('olleh')

def test_reverse_empty_string():
    """Test reversing an empty string"""
    s = []
    reverse_string_in_place(s)
    assert s == []

def test_reverse_single_char():
    """Test reversing a single character"""
    s = list('a')
    reverse_string_in_place(s)
    assert s == list('a')

def test_reverse_even_length():
    """Test reversing a string with even number of characters"""
    s = list('abcd')
    reverse_string_in_place(s)
    assert s == list('dcba')

def test_reverse_palindrome():
    """Test reversing a palindrome"""
    s = list('racecar')
    reverse_string_in_place(s)
    assert s == list('racecar')

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list of characters"):
        reverse_string_in_place("hello")
        reverse_string_in_place(123)
        reverse_string_in_place(None)