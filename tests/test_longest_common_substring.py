import pytest
from src.longest_common_substring import longest_common_substring

def test_basic_common_substring():
    """Test finding a basic common substring"""
    result = longest_common_substring("programming", "program")
    assert result == "program"
    
    result = longest_common_substring("hello", "world")
    assert result == ""

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_substring("python", "python") == "python"

def test_partial_common_substring():
    """Test finding partial common substrings"""
    assert longest_common_substring("abcdef", "bcdfgh") == "bcd"
    assert longest_common_substring("awesome", "some") == "some"

def test_empty_strings():
    """Test handling of empty strings"""
    assert longest_common_substring("", "") == ""
    assert longest_common_substring("hello", "") == ""
    assert longest_common_substring("", "world") == ""

def test_case_sensitivity():
    """Test case sensitivity of substring matching"""
    assert longest_common_substring("Hello", "hello") == ""
    assert longest_common_substring("HELLO", "hello") == ""

def test_non_string_inputs():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        longest_common_substring(123, "hello")
    with pytest.raises(TypeError):
        longest_common_substring("hello", [1, 2, 3])
    with pytest.raises(TypeError):
        longest_common_substring(None, "hello")

def test_no_common_substring():
    """Test scenario with no common substring"""
    assert longest_common_substring("xyz", "abc") == ""

def test_multiple_common_substrings():
    """Test finding the longest when multiple common substrings exist"""
    result = longest_common_substring("abcabcabc", "bcabca")
    assert result == "bcabc"  # Verify it's the specific substring we want