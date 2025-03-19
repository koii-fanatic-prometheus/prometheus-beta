import pytest
from src.palindrome_validator import is_palindrome

def test_classic_palindromes():
    """Test classic palindrome scenarios."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_edge_cases():
    """Test edge cases of palindrome validation."""
    # Empty string
    assert is_palindrome("") == True
    
    # Single character
    assert is_palindrome("a") == True
    
    # Whitespace-only string
    assert is_palindrome("   ") == True

def test_special_characters():
    """Test palindromes with various special characters."""
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("No 'x' in Nixon") == True

def test_case_insensitivity():
    """Ensure case is ignored in palindrome check."""
    assert is_palindrome("Madam") == True
    assert is_palindrome("RaceCar") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_numeric_palindromes():
    """Test numeric palindromes."""
    assert is_palindrome("123321") == True
    assert is_palindrome("1234") == False