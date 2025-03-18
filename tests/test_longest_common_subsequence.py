import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    """Test scenarios with empty strings"""
    assert longest_common_subsequence("", "") == ""
    assert longest_common_subsequence("test", "") == ""
    assert longest_common_subsequence("", "test") == ""

def test_no_common_subsequence():
    """Test strings with no common subsequence"""
    assert longest_common_subsequence("abc", "xyz") == ""

def test_identical_strings():
    """Test when both strings are identical"""
    assert longest_common_subsequence("hello", "hello") == "hello"

def test_partial_common_subsequence():
    """Test strings with partial common subsequence"""
    result = longest_common_subsequence("ABCBDAB", "BDCABA")
    # There are multiple valid LCS of length 4
    valid_results = {"BDAB", "BCBA", "BCAB"}
    assert result in valid_results

def test_case_sensitivity():
    """Test case sensitivity"""
    # Completely different case should return empty string
    assert longest_common_subsequence("HELLO", "hello") == ""
    # Partial case match should not work
    assert longest_common_subsequence("Hello", "hello") == ""
    # Different case strings with some overlap
    assert longest_common_subsequence("Hello", "Helo") == "Hel"
    assert longest_common_subsequence("hello", "Hel") == ""
    assert longest_common_subsequence("Hel", "hello") == ""

def test_unicode_strings():
    """Test with unicode strings"""
    result = longest_common_subsequence("こんにちは", "こんばんは")
    # Valid results could be "こん" or "こんは"
    valid_results = {"こん", "こんは"}
    assert result in valid_results

def test_long_strings():
    """Test with longer strings"""
    str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str2 = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    # Valid results could be "A" or "Z"
    valid_results = {"A", "Z"}
    result = longest_common_subsequence(str1, str2)
    assert result in valid_results