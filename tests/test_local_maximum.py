import pytest
from src.local_maximum import find_local_maxima

def test_basic_local_maxima():
    """Test finding local maxima in a basic array"""
    arr = [1, 3, 2, 4, 1, 5, 3]
    assert find_local_maxima(arr) == [1, 3, 5]

def test_single_element_array():
    """Test single element array always returns its index"""
    arr = [42]
    assert find_local_maxima(arr) == [0]

def test_all_increasing_array():
    """Test array that is strictly increasing"""
    arr = [1, 2, 3, 4, 5]
    assert find_local_maxima(arr) == [4]

def test_all_decreasing_array():
    """Test array that is strictly decreasing"""
    arr = [5, 4, 3, 2, 1]
    assert find_local_maxima(arr) == [0]

def test_multiple_peaks():
    """Test array with multiple local maxima"""
    arr = [1, 3, 2, 4, 1, 5, 3, 6, 2]
    assert find_local_maxima(arr) == [1, 3, 5, 7]

def test_duplicate_values():
    """Test array with duplicate values"""
    arr = [1, 3, 3, 2, 4, 4, 1]
    assert find_local_maxima(arr) == [1, 4]

def test_empty_array_raises_error():
    """Test that empty array raises ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_local_maxima([])

def test_non_list_input_raises_error():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_local_maxima("not a list")

def test_mixed_types_array():
    """Test array with mixed comparable types"""
    arr = [1, 'a', 3, 'b', 2]
    assert find_local_maxima(arr) == [2]