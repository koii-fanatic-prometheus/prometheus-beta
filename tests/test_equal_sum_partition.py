import pytest
from src.equal_sum_partition import can_partition_equal_sum

def test_partition_possible():
    """Test cases where equal partition is possible."""
    assert can_partition_equal_sum([1, 5, 11, 5]) == True
    assert can_partition_equal_sum([1, 2, 3, 5]) == False
    assert can_partition_equal_sum([2, 2, 3, 5]) == False

def test_edge_cases():
    """Test edge cases like empty list and single element list."""
    assert can_partition_equal_sum([]) == False
    assert can_partition_equal_sum([1]) == False
    assert can_partition_equal_sum([2, 2]) == True

def test_large_numbers():
    """Test cases with larger numbers."""
    assert can_partition_equal_sum([1, 2, 3, 4, 5, 6, 7]) == True
    assert can_partition_equal_sum([100, 100, 100, 100]) == True

def test_different_scenarios():
    """Test various partitioning scenarios."""
    assert can_partition_equal_sum([23, 13, 11, 7, 6, 5, 5]) == True
    assert can_partition_equal_sum([1, 2, 3, 4, 5, 6]) == False

def test_performance():
    """Test performance and handling of somewhat large inputs."""
    large_list = list(range(1, 21))  # 1 to 20
    assert can_partition_equal_sum(large_list) == True