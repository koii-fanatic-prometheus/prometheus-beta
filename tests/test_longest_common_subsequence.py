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

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence("hello", "hello") == "hello"

def test_no_common_subsequence():
    """Test strings with no common subsequence"""
    assert longest_common_subsequence("abc", "xyz") == ""

def test_partial_match():
    """Test strings with partial matches"""
    assert longest_common_subsequence("abcde", "ace") == "ace"

def test_repeated_characters():
    """Test strings with repeated characters"""
    assert longest_common_subsequence("aaaaa", "aa") == "aa"

def test_case_sensitivity():
    """Test case-sensitive comparisons"""
    assert longest_common_subsequence("Hello", "hello") == ""

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        longest_common_subsequence(123, "test")
    with pytest.raises(TypeError):
        longest_common_subsequence("test", [1, 2, 3])
    with pytest.raises(TypeError):
        longest_common_subsequence(None, "test")

def test_unicode_strings():
    """Test support for unicode strings"""
    assert longest_common_subsequence("résumé", "resumé") == "résumé"
    assert longest_common_subsequence("こんにちは", "こんばんは") == "こんは"