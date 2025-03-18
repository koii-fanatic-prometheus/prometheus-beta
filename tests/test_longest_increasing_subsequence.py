import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_standard_case():
    """Test a standard input array"""
    length, subsequence = find_longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
    assert length == 4
    assert subsequence == [2, 5, 7, 101]

def test_empty_array():
    """Test empty input array"""
    length, subsequence = find_longest_increasing_subsequence([])
    assert length == 0
    assert subsequence == []

def test_all_same_elements():
    """Test array with all same elements"""
    length, subsequence = find_longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7])
    assert length == 1
    assert subsequence == [7]

def test_already_sorted():
    """Test already sorted array"""
    length, subsequence = find_longest_increasing_subsequence([1, 2, 3, 4, 5])
    assert length == 5
    assert subsequence == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test reverse sorted array"""
    length, subsequence = find_longest_increasing_subsequence([5, 4, 3, 2, 1])
    assert length == 1
    assert subsequence == [5] or subsequence == [4] or subsequence == [3] or subsequence == [2] or subsequence == [1]

def test_multiple_possible_subsequences():
    """Test case with multiple possible longest increasing subsequences"""
    length, subsequence = find_longest_increasing_subsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
    assert length == 6
    assert subsequence == [0, 2, 6, 9, 13, 15]

def test_negative_numbers():
    """Test array with negative numbers"""
    length, subsequence = find_longest_increasing_subsequence([-7, 10, 9, 2, 3, 8, 1, 4])
    assert length == 4
    assert subsequence == [2, 3, 8, 9]