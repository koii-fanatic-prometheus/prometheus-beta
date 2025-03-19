import pytest
from src.longest_consecutive_sequence import find_longest_consecutive_sequence

def test_normal_sequence():
    """Test a list with a clear consecutive sequence"""
    assert find_longest_consecutive_sequence([100, 4, 200, 1, 3, 2]) == [1, 2, 3, 4]

def test_longer_sequence():
    """Test a longer consecutive sequence"""
    assert find_longest_consecutive_sequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def test_empty_list():
    """Test an empty list returns an empty list"""
    assert find_longest_consecutive_sequence([]) == []

def test_single_element():
    """Test a list with a single element"""
    assert find_longest_consecutive_sequence([5]) == [5]

def test_no_consecutive_sequence():
    """Test a list with no consecutive numbers"""
    assert find_longest_consecutive_sequence([5, 7, 9, 11]) == [5]

def test_duplicate_numbers():
    """Test a list with duplicate numbers"""
    assert find_longest_consecutive_sequence([1, 2, 2, 3, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negative_numbers():
    """Test a list with negative numbers"""
    assert find_longest_consecutive_sequence([-3, -2, -1, 0, 1, 3, 4, 5]) == [-3, -2, -1, 0, 1]