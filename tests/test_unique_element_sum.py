import pytest
from src.unique_element_sum import sum_unique_elements

def test_sum_unique_elements_basic():
    """Test basic functionality of sum_unique_elements"""
    assert sum_unique_elements([1, 2, 3, 2]) == 4  # 1+3 = 4
    assert sum_unique_elements([1, 1, 1, 1]) == 0  # No unique elements
    assert sum_unique_elements([]) == 0

def test_sum_unique_elements_complex():
    """Test more complex scenarios"""
    assert sum_unique_elements([4, 4, 5, 5, 6, 6]) == 0  # No unique elements
    assert sum_unique_elements([1, 2, 3, 4, 5]) == 15  # All unique

def test_sum_unique_elements_edge_cases():
    """Test edge cases"""
    assert sum_unique_elements([0]) == 0
    assert sum_unique_elements([-1, -1, 2, 2]) == 0
    assert sum_unique_elements([1, -1, 2, -2, 3]) == 0  # No unique elements

def test_sum_unique_elements_large_numbers():
    """Test with large numbers"""
    assert sum_unique_elements([10000, 10000, 20000, 20000]) == 0
    assert sum_unique_elements([1000000, 1000001, 1000002]) == 3000003

def test_sum_unique_elements_types():
    """Ensure function handles different input types gracefully"""
    with pytest.raises(TypeError):
        sum_unique_elements(["1", "2", "3"])
    with pytest.raises(TypeError):
        sum_unique_elements([1, "2", 3])