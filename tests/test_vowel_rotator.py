import pytest
from src.vowel_rotator import rotate_vowels

def test_basic_vowel_rotation():
    """Test basic vowel rotation in lowercase"""
    assert rotate_vowels("hello") == "holli"
    assert rotate_vowels("python") == "pythin"

def test_uppercase_vowel_rotation():
    """Test vowel rotation preserving uppercase"""
    assert rotate_vowels("HELLO") == "HOLLI"
    assert rotate_vowels("AEIOU") == "EIOUA"

def test_mixed_case_rotation():
    """Test vowel rotation in mixed case strings"""
    assert rotate_vowels("Hello World") == "Holli Wirld"
    assert rotate_vowels("PyThOn") == "PiThIn"

def test_no_vowels():
    """Test strings without vowels"""
    assert rotate_vowels("xyz") == "xyz"
    assert rotate_vowels("123") == "123"

def test_empty_string():
    """Test empty string input"""
    assert rotate_vowels("") == ""

def test_all_vowel_circular_rotation():
    """Verify circular rotation of all vowels"""
    # a -> e -> i -> o -> u -> a
    assert rotate_vowels("aeiou") == "eioua"
    assert rotate_vowels("AEIOU") == "EIOUA"