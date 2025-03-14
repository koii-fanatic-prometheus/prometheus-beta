import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic removal of duplicate integers"""
    assert remove_duplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_empty_list():
    """Test behavior with an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_all_same():
    """Test list with all identical elements"""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_remove_duplicates_mixed_types():
    """Test with mixed order of duplicates"""
    assert remove_duplicates([5, 2, 3, 2, 5, 1, 3]) == [5, 2, 3, 1]

def test_remove_duplicates_order_preservation():
    """Ensure first occurrence order is preserved"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = [3, 1, 4, 5, 9, 2, 6]
    assert remove_duplicates(input_list) == expected