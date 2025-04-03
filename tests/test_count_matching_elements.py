import pytest
from src.count_matching_elements import count_matching_elements

def test_basic_matching():
    """Test basic matching of elements"""
    assert count_matching_elements([1, 2, 3], [2, 3, 4]) == 2

def test_empty_arrays():
    """Test with empty arrays"""
    assert count_matching_elements([], [1, 2, 3]) == 0
    assert count_matching_elements([1, 2, 3], []) == 0
    assert count_matching_elements([], []) == 0

def test_duplicate_elements():
    """Test with duplicate elements"""
    assert count_matching_elements([1, 1, 2], [1, 2, 2]) == 3

def test_no_matching_elements():
    """Test with no matching elements"""
    assert count_matching_elements([1, 2, 3], [4, 5, 6]) == 0

def test_type_error_non_list():
    """Test type error when inputs are not lists"""
    with pytest.raises(TypeError, match="Both inputs must be lists"):
        count_matching_elements(123, [1, 2, 3])
    with pytest.raises(TypeError, match="Both inputs must be lists"):
        count_matching_elements([1, 2, 3], "not a list")

def test_type_error_non_integers():
    """Test type error when elements are not integers"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        count_matching_elements([1, 2, '3'], [1, 2, 3])
    with pytest.raises(TypeError, match="All elements must be integers"):
        count_matching_elements([1, 2, 3], [1, 2, '3'])