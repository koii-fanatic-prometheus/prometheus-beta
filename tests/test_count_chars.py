import pytest
from src.count_chars import count_vowels_consonants

def test_basic_string():
    """Test a basic string with mixed vowels and consonants."""
    result = count_vowels_consonants("hello")
    assert result == {'vowels': 2, 'consonants': 3}

def test_empty_string():
    """Test an empty string."""
    result = count_vowels_consonants("")
    assert result == {'vowels': 0, 'consonants': 0}

def test_only_vowels():
    """Test a string with only vowels."""
    result = count_vowels_consonants("aeiou")
    assert result == {'vowels': 5, 'consonants': 0}

def test_only_consonants():
    """Test a string with only consonants."""
    result = count_vowels_consonants("xyz")
    assert result == {'vowels': 0, 'consonants': 3}

def test_mixed_case():
    """Test a string with mixed case letters."""
    result = count_vowels_consonants("HeLLo WoRLd")
    assert result == {'vowels': 3, 'consonants': 7}

def test_with_spaces_and_punctuation():
    """Test a string with spaces and punctuation."""
    result = count_vowels_consonants("Hello, World! 123")
    assert result == {'vowels': 3, 'consonants': 7}

def test_non_alphabetic_input():
    """Ensure only alphabetic characters are counted."""
    result = count_vowels_consonants("123!@#")
    assert result == {'vowels': 0, 'consonants': 0}

def test_invalid_input_type():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        count_vowels_consonants(None)