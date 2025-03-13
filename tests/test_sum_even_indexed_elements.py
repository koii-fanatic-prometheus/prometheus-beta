import pytest
from src.sum_even_indexed_elements import sum_even_indexed_elements

def test_sum_even_indexed_elements():
    """Test various scenarios for sum_even_indexed_elements function."""
    # Test with positive integers
    assert sum_even_indexed_elements([1, 2, 3, 4, 5]) == 9, "Failed with positive integers"
    
    # Test with mixed positive and negative integers
    assert sum_even_indexed_elements([-1, 2, -3, 4, -5]) == -9, "Failed with mixed integers"
    
    # Test with empty list
    assert sum_even_indexed_elements([]) == 0, "Failed with empty list"
    
    # Test with single element
    assert sum_even_indexed_elements([42]) == 42, "Failed with single element"
    
    # Test with even number of elements
    assert sum_even_indexed_elements([1, 10, 2, 20, 3, 30]) == 6, "Failed with even number of elements"
    
    # Test with all zero elements
    assert sum_even_indexed_elements([0, 1, 0, 2, 0, 3]) == 0, "Failed with zero elements"

def test_sum_even_indexed_elements_types():
    """Test type handling and error cases."""
    # Test invalid input types
    with pytest.raises(TypeError):
        sum_even_indexed_elements(None)
    
    with pytest.raises(TypeError):
        sum_even_indexed_elements("not a list")
    
    with pytest.raises(TypeError):
        sum_even_indexed_elements([1, '2', 3])