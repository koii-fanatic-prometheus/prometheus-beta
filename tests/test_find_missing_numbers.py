import pytest
from src.find_missing_numbers import find_missing_numbers

def test_find_missing_numbers_basic():
    """Test finding missing numbers in a basic scenario"""
    assert find_missing_numbers([1, 3, 5]) == [2, 4]

def test_find_missing_numbers_consecutive():
    """Test array with no missing numbers"""
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_find_missing_numbers_negative():
    """Test with negative and positive numbers"""
    assert find_missing_numbers([-3, -1, 0, 2, 4]) == [-2, 1, 3]

def test_find_missing_numbers_empty():
    """Test with empty array"""
    assert find_missing_numbers([]) == []

def test_find_missing_numbers_single():
    """Test with single number in array"""
    assert find_missing_numbers([5]) == [6, 7, 8, 9, 10]

def test_find_missing_numbers_invalid_input():
    """Test invalid input types"""
    with pytest.raises(TypeError):
        find_missing_numbers("not a list")
    
    with pytest.raises(TypeError):
        find_missing_numbers(123)

def test_find_missing_numbers_duplicates():
    """Test input with duplicate numbers"""
    with pytest.raises(ValueError):
        find_missing_numbers([1, 2, 2, 3])