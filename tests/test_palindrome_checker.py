import pytest
from src.palindrome_checker import is_palindrome

def test_palindrome_basic():
    """Test basic palindrome cases"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False

def test_palindrome_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_palindrome_case_insensitive():
    """Test case insensitivity"""
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_palindrome_empty_and_single_char():
    """Test empty string and single character"""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True

def test_palindrome_with_numbers():
    """Test palindromes with numbers"""
    assert is_palindrome("1221") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("123") == False

def test_palindrome_mixed_alphanumeric():
    """Test mixed alphanumeric palindromes"""
    assert is_palindrome("a1b22b1a") == True
    assert is_palindrome("a1b2c3") == False

def test_palindrome_special_chars():
    """Test handling of special characters"""
    assert is_palindrome("!@#$a1b1a$#@!") == True
    assert is_palindrome("hello!!") == False