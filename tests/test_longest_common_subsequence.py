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
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence("Hello", "hello") == ""
    assert longest_common_subsequence("Hello", "Helo") == "Hel"

def test_unicode_strings():
    """Test with unicode strings"""
    assert longest_common_subsequence("こんにちは", "こんばんは") == "こん"

def test_long_strings():
    """Test with longer strings"""
    str1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str2 = "ZYXWVUTSRQPONMLKJIHGFEDCBA"
    assert longest_common_subsequence(str1, str2) == "A"