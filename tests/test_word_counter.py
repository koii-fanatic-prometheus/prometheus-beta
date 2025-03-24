import pytest
from src.word_counter import count_words

def test_normal_string():
    """Test counting words in a normal string."""
    assert count_words("Hello world") == 2

def test_multiple_spaces():
    """Test string with multiple spaces between words."""
    assert count_words("Hello   world  test") == 3

def test_leading_trailing_spaces():
    """Test string with leading and trailing spaces."""
    assert count_words("  Hello world  ") == 2

def test_empty_string():
    """Test empty string returns zero words."""
    assert count_words("") == 0

def test_whitespace_only():
    """Test string with only whitespace returns zero words."""
    assert count_words("   \t\n  ") == 0

def test_none_input():
    """Test None input returns zero words."""
    assert count_words(None) == 0

def test_numbers_and_punctuation():
    """Test string with numbers and punctuation."""
    assert count_words("Hello, world! 123 test.") == 4

def test_non_string_input():
    """Test non-string input is converted to string."""
    assert count_words(12345) == 1
    assert count_words(["hello", "world"]) == 1

def test_unicode_words():
    """Test counting words with unicode characters."""
    assert count_words("こんにちは 世界") == 2
    assert count_words("Hello Привет") == 2