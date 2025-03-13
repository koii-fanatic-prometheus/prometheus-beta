import pytest
from src.two_sum import find_two_sum_indices

def test_two_sum_basic_case():
    """Test basic case where solution exists"""
    nums = [2, 7, 11, 15]
    target = 9
    assert sorted(find_two_sum_indices(nums, target)) == [0, 1]

def test_two_sum_end_of_array():
    """Test case where solution is at the end of the array"""
    nums = [3, 2, 4]
    target = 6
    assert sorted(find_two_sum_indices(nums, target)) == [1, 2]

def test_two_sum_no_solution():
    """Test case where no solution exists"""
    nums = [1, 2, 3, 4]
    target = 10
    assert find_two_sum_indices(nums, target) == []

def test_two_sum_duplicate_numbers():
    """Test case with duplicate numbers"""
    nums = [3, 3]
    target = 6
    assert sorted(find_two_sum_indices(nums, target)) == [0, 1]

def test_two_sum_negative_numbers():
    """Test case with negative numbers"""
    nums = [-1, -2, -3, -4, -5]
    target = -8
    assert sorted(find_two_sum_indices(nums, target)) == [2, 4]

def test_two_sum_invalid_input_not_list():
    """Test error handling for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_two_sum_indices("not a list", 10)

def test_two_sum_invalid_target():
    """Test error handling for invalid target type"""
    with pytest.raises(TypeError, match="Target must be a numeric value"):
        find_two_sum_indices([1, 2, 3], "not a number")

def test_two_sum_non_numeric_list():
    """Test error handling for list with non-numeric elements"""
    with pytest.raises(ValueError, match="List must contain only numeric elements"):
        find_two_sum_indices([1, 2, "3"], 6)

def test_two_sum_empty_list():
    """Test behavior with an empty list"""
    nums = []
    target = 10
    assert find_two_sum_indices(nums, target) == []

def test_two_sum_large_list():
    """Test with a larger list to ensure efficiency"""
    nums = list(range(1000)) + [1000, 2000]
    target = 3000
    assert sorted(find_two_sum_indices(nums, target)) == [1000, 1001]