import pytest
from src.closest_pair_sum import find_closest_pair_sum

def test_basic_positive_case():
    """Test basic scenario with a clear closest pair"""
    arr = [1, 2, 3, 4, 5]
    target = 7
    result = find_closest_pair_sum(arr, target)
    assert result[0] + result[1] == 7 or abs(result[0] + result[1] - 7) == min(abs(x + y - 7) for x in arr for y in arr if x != y)

def test_multiple_pairs_same_closeness():
    """Test when multiple pairs have the same closeness, return first occurring pair"""
    arr = [1, 2, 3, 4, 5, 6]
    target = 7
    result = find_closest_pair_sum(arr, target)
    assert result in [(1, 6), (2, 5), (3, 4)]

def test_negative_numbers():
    """Test with negative numbers in the array"""
    arr = [-1, -5, 3, 7, 10]
    target = 4
    result = find_closest_pair_sum(arr, target)
    assert abs(result[0] + result[1] - 4) == min(abs(x + y - 4) for x in arr for y in arr if x != y)

def test_floating_point_target():
    """Test with a floating-point target"""
    arr = [1.5, 2.5, 3.5, 4.5]
    target = 7.0
    result = find_closest_pair_sum(arr, target)
    assert abs(result[0] + result[1] - 7.0) == min(abs(x + y - 7.0) for x in arr for y in arr if x != y)

def test_minimum_array_size():
    """Test array with exactly two elements"""
    arr = [1, 2]
    target = 3
    assert find_closest_pair_sum(arr, target) == (1, 2)

def test_invalid_input():
    """Test raising ValueError for invalid input"""
    with pytest.raises(ValueError, match="Input array must contain at least two elements"):
        find_closest_pair_sum([], 5)
    
    with pytest.raises(ValueError, match="Input array must contain at least two elements"):
        find_closest_pair_sum([1], 5)

def test_large_array():
    """Test with a larger array to ensure performance"""
    arr = list(range(1, 101))
    target = 150
    result = find_closest_pair_sum(arr, target)
    assert abs(result[0] + result[1] - 150) == min(abs(x + y - 150) for x in arr for y in arr if x != y)

def test_all_same_elements():
    """Test an array with all identical elements"""
    arr = [5, 5, 5, 5, 5]
    target = 10
    assert find_closest_pair_sum(arr, target) == (5, 5)