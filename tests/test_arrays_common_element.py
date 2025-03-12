import pytest
from src.arrays_common_element import has_common_element

def test_arrays_with_common_element():
    """Test arrays that have a common element"""
    assert has_common_element([1, 2, 3], [3, 4, 5]) == True
    assert has_common_element([1, 2, 3], [4, 5, 1]) == True
    assert has_common_element(['a', 'b'], ['b', 'c']) == True

def test_arrays_without_common_element():
    """Test arrays without a common element"""
    assert has_common_element([1, 2, 3], [4, 5, 6]) == False
    assert has_common_element([1, 2, 3], ['a', 'b', 'c']) == False

def test_edge_cases():
    """Test edge cases like empty arrays"""
    assert has_common_element([], [1, 2, 3]) == False
    assert has_common_element([1, 2, 3], []) == False
    assert has_common_element([], []) == False

def test_different_types():
    """Test arrays with different element types"""
    assert has_common_element([1, 2, 3], [3.0, 4, 5]) == True
    assert has_common_element(['1', 1], [1, '2']) == False