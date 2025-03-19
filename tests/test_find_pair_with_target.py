import pytest
from src.find_pair_with_target import find_pair_with_target

def test_find_pair_with_target_basic():
    """Test basic functionality of finding index pairs."""
    nums = [10, 5, 2, 3, 7, 5]
    target = 10
    assert sorted(find_pair_with_target(nums, target)) == [(1, 4), (2, 3)]

def test_find_pair_with_target_no_pairs():
    """Test when no pairs sum to target."""
    nums = [1, 2, 3, 4, 5]
    target = 20
    assert find_pair_with_target(nums, target) == []

def test_find_pair_with_target_single_solution():
    """Test when there's only one pair summing to target."""
    nums = [1, 4, 5, 3, 2]
    target = 7
    assert find_pair_with_target(nums, target) == [(1, 2)]

def test_find_pair_with_target_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        find_pair_with_target("not a list", 10)
    
    with pytest.raises(TypeError):
        find_pair_with_target([1, 2, 3], "not an int")

def test_find_pair_with_target_empty_list():
    """Test error handling for empty list."""
    with pytest.raises(ValueError):
        find_pair_with_target([], 10)

def test_find_pair_with_target_all_same_number():
    """Test case with repeated numbers."""
    nums = [5, 5, 5, 5]
    target = 10
    assert sorted(find_pair_with_target(nums, target)) == [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

def test_find_pair_with_target_negative_numbers():
    """Test functionality with negative numbers."""
    nums = [-1, -2, 3, 4, 5, -3]
    target = 1
    assert sorted(find_pair_with_target(nums, target)) == [(0, 2), (1, 4), (3, 5)]