import pytest
from src.anagram_checker import anagram_checker

def test_basic_anagrams():
    """Test basic anagram cases"""
    assert anagram_checker("listen", "silent") == True
    assert anagram_checker("hello", "olleh") == True

def test_non_anagrams():
    """Test words that are not anagrams"""
    assert anagram_checker("hello", "world") == False
    assert anagram_checker("python", "java") == False

def test_case_insensitive():
    """Test that the function is case-insensitive"""
    assert anagram_checker("Listen", "Silent") == True
    assert anagram_checker("Debit Card", "Bad Credit") == True

def test_whitespace_handling():
    """Test that whitespace is ignored"""
    assert anagram_checker("debit card", "bad credit") == True
    assert anagram_checker(" listen", "silent ") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert anagram_checker("", "") == True

def test_type_errors():
    """Test type error handling"""
    with pytest.raises(TypeError):
        anagram_checker(123, "hello")
    with pytest.raises(TypeError):
        anagram_checker("hello", None)
    with pytest.raises(TypeError):
        anagram_checker([], "hello")

def test_unicode_characters():
    """Test handling of Unicode characters"""
    assert anagram_checker("résumé", "summer") == False
    assert anagram_checker("café", "face") == False