import pytest
from src.longest_palindrome_subsequence import longest_palindrome_subsequence

def test_longest_palindrome_subsequence():
    # Test cases from the function docstring
    assert longest_palindrome_subsequence("bbbab") == 4
    assert longest_palindrome_subsequence("cbbd") == 2

def test_edge_cases():
    # Empty string
    assert longest_palindrome_subsequence("") == 0
    
    # Single character
    assert longest_palindrome_subsequence("a") == 1
    assert longest_palindrome_subsequence("z") == 1

def test_various_scenarios():
    # Entire string is a palindrome
    assert longest_palindrome_subsequence("racecar") == 7
    
    # No characters match to form a palindrome
    assert longest_palindrome_subsequence("abcdef") == 1
    
    # Multiple possible subsequences
    assert longest_palindrome_subsequence("aabaa") == 5
    assert longest_palindrome_subsequence("forgeeksskeegfor") == 12

def test_mixed_characters():
    # Mixed case
    assert longest_palindrome_subsequence("AbcbA") == 5
    
    # With repeated characters
    assert longest_palindrome_subsequence("aabbccddccbbaa") == 14

def test_long_input():
    # Longer input to test performance and correctness
    long_input = "a" * 1000 + "b" * 1000
    assert longest_palindrome_subsequence(long_input) == 1000