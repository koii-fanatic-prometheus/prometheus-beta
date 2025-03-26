import pytest
from src.two_sum import find_two_sum_pairs

def test_basic_two_sum_pairs():
    """Test finding pairs in a basic scenario"""
    numbers = [1, 2, 3, 4, 5]
    target_sum = 7
    expected = [(2, 5), (3, 4)]
    assert sorted(find_two_sum_pairs(numbers, target_sum)) == sorted(expected)

def test_multiple_pairs_same_target():
    """Test scenario with multiple pairs summing to the same target"""
    numbers = [1, 5, 3, 4, 2, 6]
    target_sum = 7
    expected = [(1, 6), (2, 5), (3, 4)]
    assert sorted(find_two_sum_pairs(numbers, target_sum)) == sorted(expected)

def test_no_pairs_found():
    """Test scenario where no pairs sum to the target"""
    numbers = [1, 2, 3, 4, 5]
    target_sum = 10
    assert find_two_sum_pairs(numbers, target_sum) == []

def test_only_one_pair():
    """Test scenario with only one pair summing to the target"""
    numbers = [1, 2, 3, 4, 5]
    target_sum = 9
    expected = [(4, 5)]
    assert find_two_sum_pairs(numbers, target_sum) == expected

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_two_sum_pairs([], 10)

def test_none_input_raises_error():
    """Test that None input raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be None"):
        find_two_sum_pairs(None, 10)

def test_non_integer_list_raises_error():
    """Test that a list with non-integer elements raises a TypeError"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_two_sum_pairs([1, 2, 'three', 4], 10)

def test_target_zero():
    """Test scenario with target sum of zero"""
    numbers = [-1, 0, 1, 2, -2]
    target_sum = 0
    expected = [(-1, 1), (-2, 2)]
    assert sorted(find_two_sum_pairs(numbers, target_sum)) == sorted(expected)

def test_large_list():
    """Test performance and correctness with a larger list"""
    numbers = list(range(1, 101))
    target_sum = 50
    expected = [(i, target_sum - i) for i in range(1, 50) if i < target_sum - i]
    assert sorted(find_two_sum_pairs(numbers, target_sum)) == sorted(expected)