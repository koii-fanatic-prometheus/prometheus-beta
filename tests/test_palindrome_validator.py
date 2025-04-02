import pytest
from src.palindrome_validator import is_palindrome

def test_valid_palindromes():
    """Test various valid palindromes with different formatting."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_case_sensitivity():
    """Test that function is case-insensitive."""
    assert is_palindrome("Madam") == True
    assert is_palindrome("MaDaM") == True

def test_special_characters():
    """Test handling of special characters and spaces."""
    assert is_palindrome("!@#$%^&*()") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("No 'x' in Nixon") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_edge_cases():
    """Test edge cases like single character and whitespace."""
    assert is_palindrome(" ") == True
    assert is_palindrome("a") == True
    assert is_palindrome("  a  ") == True

def test_input_types():
    """Test error handling for different input types."""
    with pytest.raises(AttributeError):
        is_palindrome(None)
    with pytest.raises(AttributeError):
        is_palindrome(123)