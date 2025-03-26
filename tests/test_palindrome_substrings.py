import pytest
from src.palindrome_substrings import count_palindromic_substrings

def test_empty_string():
    """Test counting palindromes in an empty string."""
    assert count_palindromic_substrings("") == 0

def test_single_character():
    """Test a single character is always a palindrome."""
    assert count_palindromic_substrings("a") == 1

def test_two_different_characters():
    """Test a string with two different characters."""
    assert count_palindromic_substrings("ab") == 2

def test_repeated_characters():
    """Test a string with repeated characters."""
    assert count_palindromic_substrings("aaa") == 6

def test_mixed_palindromes():
    """Test a string with mix of palindromic and non-palindromic substrings."""
    assert count_palindromic_substrings("abc") == 3

def test_longer_palindromic_string():
    """Test a longer string with multiple palindromes."""
    assert count_palindromic_substrings("racecar") == 10

def test_complex_palindrome():
    """Test a complex string with various palindromic substrings."""
    assert count_palindromic_substrings("aabaa") == 9

def test_no_repeats():
    """Test a string with no repeated characters."""
    assert count_palindromic_substrings("abcde") == 5

def test_alternating_characters():
    """Test a string with alternating characters."""
    assert count_palindromic_substrings("xyxyx") == 9