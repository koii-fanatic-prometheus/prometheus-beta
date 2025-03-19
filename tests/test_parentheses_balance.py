import pytest
from src.parentheses_balance import is_balanced_parentheses

def test_balanced_single_pair():
    assert is_balanced_parentheses("()") == True

def test_balanced_nested():
    assert is_balanced_parentheses("((()))") == True

def test_balanced_multiple_pairs():
    assert is_balanced_parentheses("(()())") == True

def test_unbalanced_extra_opening():
    assert is_balanced_parentheses("((()") == False

def test_unbalanced_extra_closing():
    assert is_balanced_parentheses("())") == False

def test_unbalanced_reversed():
    assert is_balanced_parentheses(")(") == False

def test_empty_string():
    assert is_balanced_parentheses("") == True

def test_complex_balanced():
    assert is_balanced_parentheses("((()())(()))") == True

def test_unbalanced_complex():
    assert is_balanced_parentheses("((()())(()") == False

def test_only_opening_parentheses():
    assert is_balanced_parentheses("(((") == False

def test_only_closing_parentheses():
    assert is_balanced_parentheses(")))") == False