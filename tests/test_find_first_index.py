import pytest
from src.find_first_index import find_first_index

def test_find_first_index_basic():
    """Test basic functionality of finding an existing element."""
    assert find_first_index([1, 2, 3, 4, 3], 3) == 2

def test_find_first_index_not_found():
    """Test when target is not in the list."""
    assert find_first_index([1, 2, 4, 5], 3) == -1

def test_find_first_index_empty_list():
    """Test behavior with an empty list."""
    assert find_first_index([], 1) == -1

def test_find_first_index_first_element():
    """Test finding the first element."""
    assert find_first_index([5, 2, 3, 4, 5], 5) == 0

def test_find_first_index_last_element():
    """Test finding the last element."""
    assert find_first_index([1, 2, 3, 4, 5], 5) == 4

def test_find_first_index_multiple_occurrences():
    """Test when target appears multiple times."""
    assert find_first_index([1, 2, 3, 2, 4], 2) == 1

def test_find_first_index_invalid_input():
    """Test handling of invalid input types."""
    with pytest.raises(TypeError):
        find_first_index(None, 1)
    
    with pytest.raises(TypeError):
        find_first_index("not a list", 1)

def test_find_first_index_different_types():
    """Test finding elements of different types."""
    assert find_first_index([1, 2, 3, 4], 3) == 2
    assert find_first_index([-1, 0, 1], 0) == 1
    assert find_first_index([0, -1, 1], -1) == 1