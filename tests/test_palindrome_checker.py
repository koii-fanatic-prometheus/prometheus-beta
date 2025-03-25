import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("") == True

def test_case_insensitive_palindromes():
    """Test palindromes with mixed case."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_numeric_palindromes():
    """Test palindromes with numbers."""
    assert is_palindrome("12321") == True
    assert is_palindrome("45654") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    assert is_palindrome("python") == False

def test_palindromes_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation."""
    assert is_palindrome("race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_single_character():
    """Test single character input."""
    assert is_palindrome("a") == True
    assert is_palindrome("1") == True

def test_whitespace_and_empty_string():
    """Test whitespace and empty string inputs."""
    assert is_palindrome("") == True
    assert is_palindrome("   ") == True
    assert is_palindrome("\t\n") == True