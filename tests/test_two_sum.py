import pytest
from src.two_sum import find_two_sum

def test_basic_find_two_sum():
    """Test finding two numbers that sum to a target."""
    nums = [2, 7, 11, 15]
    target = 9
    result = find_two_sum(nums, target)
    assert result == (0, 1)

def test_find_two_sum_end_of_array():
    """Test finding numbers at the end of the array."""
    nums = [3, 2, 4]
    target = 6
    result = find_two_sum(nums, target)
    assert result == (1, 2)

def test_find_two_sum_no_solution():
    """Test when no solution exists."""
    nums = [1, 2, 3, 4]
    target = 10
    result = find_two_sum(nums, target)
    assert result is None

def test_find_two_sum_duplicate_numbers():
    """Test when numbers might be the same."""
    nums = [3, 3]
    target = 6
    result = find_two_sum(nums, target)
    assert result == (0, 1)

def test_find_two_sum_empty_list():
    """Test with an empty list."""
    nums = []
    target = 5
    result = find_two_sum(nums, target)
    assert result is None

def test_find_two_sum_negative_numbers():
    """Test with negative numbers."""
    nums = [-1, -2, -3, -4, -5]
    target = -8
    result = find_two_sum(nums, target)
    assert result == (2, 4)

def test_find_two_sum_invalid_input_not_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_two_sum(123, 10)

def test_find_two_sum_invalid_list_elements():
    """Test raising TypeError for non-numeric elements."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_two_sum([1, 2, 'a'], 5)

def test_find_two_sum_first_occurrence():
    """Ensure first occurrence is returned if multiple pairs exist."""
    nums = [3, 3, 3]
    target = 6
    result = find_two_sum(nums, target)
    assert result == (0, 1)