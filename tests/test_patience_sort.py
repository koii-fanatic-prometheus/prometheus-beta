import pytest
from src.patience_sort import patience_sort

def test_patience_sort_basic():
    """Test basic sorting of integer list"""
    input_list = [5, 2, 8, 12, 1, 6]
    expected = sorted(input_list)
    assert patience_sort(input_list) == expected

def test_patience_sort_already_sorted():
    """Test list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert patience_sort(input_list) == input_list

def test_patience_sort_reverse_sorted():
    """Test list sorted in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert patience_sort(input_list) == expected

def test_patience_sort_duplicate_elements():
    """Test list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected = sorted(input_list)
    assert patience_sort(input_list) == expected

def test_patience_sort_empty_list():
    """Test empty list"""
    assert patience_sort([]) == []

def test_patience_sort_single_element():
    """Test list with single element"""
    input_list = [42]
    assert patience_sort(input_list) == input_list

def test_patience_sort_strings():
    """Test sorting strings"""
    input_list = ['banana', 'apple', 'cherry', 'date']
    expected = sorted(input_list)
    assert patience_sort(input_list) == expected

def test_patience_sort_mixed_types():
    """Test sorting with mixed comparable types"""
    input_list = [5, 2, 'a', 'b', 1, 'c']
    expected = sorted(input_list)
    assert patience_sort(input_list) == expected

def test_patience_sort_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        patience_sort("not a list")

def test_patience_sort_non_comparable():
    """Test list with non-comparable elements"""
    class NonComparable:
        pass
    
    input_list = [NonComparable(), NonComparable()]
    with pytest.raises(TypeError):
        patience_sort(input_list)