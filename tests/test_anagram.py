import pytest
from src.anagram import is_anagram

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("triangle", "integral") == True

def test_non_anagrams():
    """Test strings that are not anagrams"""
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False

def test_case_insensitive():
    """Test that anagram check is case-insensitive"""
    assert is_anagram("Tea", "Eat") == True
    assert is_anagram("LISTEN", "silent") == True

def test_whitespace_handling():
    """Test that whitespace is ignored"""
    assert is_anagram("debit card", "bad credit") == True
    assert is_anagram("a gentleman", "elegant man") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert is_anagram("", "") == True

def test_different_lengths():
    """Test strings of different lengths"""
    assert is_anagram("abc", "abcd") == False

def test_invalid_inputs():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        is_anagram(123, "abc")
    with pytest.raises(TypeError):
        is_anagram("abc", None)

def test_unicode_characters():
    """Test anagram detection with unicode characters"""
    assert is_anagram("über", "rebü") == True