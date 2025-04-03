import pytest
from src.palindrome import is_palindrome

def test_is_palindrome_basic_palindromes():
    """Test basic palindrome strings"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_is_palindrome_edge_cases():
    """Test edge cases for palindrome function"""
    # Empty string is considered a palindrome
    assert is_palindrome("") == True
    
    # Single character is a palindrome
    assert is_palindrome("a") == True
    
    # Strings with spaces and punctuation
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("hello world") == False

def test_is_palindrome_case_sensitivity():
    """Test case-insensitive palindrome checking"""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RACECAR") == True
    assert is_palindrome("RaCeCaR") == True

def test_is_palindrome_with_special_characters():
    """Test palindromes with various special characters"""
    assert is_palindrome("!@#$A man, a plan, a canal: Panama@#$!") == True
    assert is_palindrome("No 'x' in Nixon") == True
    assert is_palindrome("abc123321cba") == True
    assert is_palindrome("hello123321world") == False

def test_is_palindrome_non_string_input():
    """Verify appropriate handling of non-string inputs"""
    with pytest.raises(AttributeError):
        is_palindrome(12321)
    with pytest.raises(AttributeError):
        is_palindrome(None)