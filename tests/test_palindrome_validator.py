import pytest
from src.palindrome_validator import is_palindrome

def test_simple_palindromes():
    """Test basic palindrome strings."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("radar") == True

def test_case_insensitive_palindromes():
    """Test palindromes with mixed case."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_empty_and_single_char():
    """Test edge cases with empty and single character strings."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_with_punctuation():
    """Test palindromes with punctuation and spaces."""
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("race a car") == False

def test_invalid_input():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome(123)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])