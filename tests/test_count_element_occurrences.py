import pytest
from src.count_element_occurrences import count_element_occurrences

def test_count_element_occurrences():
    # Test basic functionality
    assert count_element_occurrences([1, 2, 3, 2, 4, 2], 2) == 3
    assert count_element_occurrences(['a', 'b', 'a', 'c', 'a'], 'a') == 3
    
    # Test with empty list
    assert count_element_occurrences([], 5) == 0
    
    # Test with no occurrences
    assert count_element_occurrences([1, 2, 3, 4], 5) == 0
    
    # Test with different types
    assert count_element_occurrences([1, 'a', 1, 'b', 1], 1) == 3
    
    # Test with None
    assert count_element_occurrences([None, 1, None, 2], None) == 2

def test_count_element_occurrences_error_handling():
    # Test non-list input raises TypeError
    with pytest.raises(TypeError, match="Input must be a list"):
        count_element_occurrences("not a list", 1)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        count_element_occurrences(123, 1)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        count_element_occurrences(None, 1)