import pytest
from src.is_palindrome import is_palindrome

def test_empty_list():
    """Test that an empty list is considered a palindrome"""
    assert is_palindrome([]) is True

def test_single_element_list():
    """Test that a single-element list is a palindrome"""
    assert is_palindrome([1]) is True
    assert is_palindrome([42]) is True

def test_palindrome_even_length():
    """Test palindrome lists with even number of elements"""
    assert is_palindrome([1, 2, 2, 1]) is True
    assert is_palindrome([5, 7, 7, 5]) is True

def test_palindrome_odd_length():
    """Test palindrome lists with odd number of elements"""
    assert is_palindrome([1, 2, 1]) is True
    assert is_palindrome([5, 7, 5]) is True

def test_non_palindrome():
    """Test lists that are not palindromes"""
    assert is_palindrome([1, 2, 3]) is False
    assert is_palindrome([1, 2, 4, 3]) is False

def test_mixed_types_palindrome():
    """Test palindrome with mixed integer values"""
    assert is_palindrome([10, 20, 30, 20, 10]) is True
    assert is_palindrome([0, -5, 0]) is True

def test_invalid_input_type():
    """Test that non-list inputs raise TypeError"""
    with pytest.raises(TypeError):
        is_palindrome(123)
    
    with pytest.raises(TypeError):
        is_palindrome("not a list")
    
    with pytest.raises(TypeError):
        is_palindrome(None)