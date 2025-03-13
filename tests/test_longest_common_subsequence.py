import pytest
from src.longest_common_subsequence import longest_common_subsequence_length

def test_basic_lcs():
    """Test basic longest common subsequence scenarios"""
    assert longest_common_subsequence_length("ABCDGH", "AEDFHR") == 3
    assert longest_common_subsequence_length("AGGTAB", "GXTXAYB") == 4

def test_empty_strings():
    """Test scenarios with empty strings"""
    assert longest_common_subsequence_length("", "") == 0
    assert longest_common_subsequence_length("ABC", "") == 0
    assert longest_common_subsequence_length("", "XYZ") == 0

def test_identical_strings():
    """Test when strings are identical"""
    assert longest_common_subsequence_length("HELLO", "HELLO") == 5
    assert longest_common_subsequence_length("", "") == 0

def test_no_common_subsequence():
    """Test strings with no common subsequence"""
    assert longest_common_subsequence_length("ABC", "XYZ") == 0

def test_partial_matching():
    """Test strings with partial matching"""
    assert longest_common_subsequence_length("ABCBDAB", "BDCABA") == 4
    assert longest_common_subsequence_length("XMJYAUZ", "MZJAWXU") == 4

def test_single_character_match():
    """Test scenarios with single character matches"""
    assert longest_common_subsequence_length("A", "A") == 1
    assert longest_common_subsequence_length("A", "B") == 0

def test_case_sensitivity():
    """Test case sensitivity"""
    assert longest_common_subsequence_length("Hello", "hello") == 0
    assert longest_common_subsequence_length("AbC", "AbC") == 3

def test_repeated_characters():
    """Test strings with repeated characters"""
    assert longest_common_subsequence_length("AAAAAA", "AAAAAA") == 6
    assert longest_common_subsequence_length("ABABAB", "ABAB") == 4