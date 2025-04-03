import pytest
from src.delete_duplicates import deleteDuplicates

def test_delete_duplicates_normal_case():
    """Test removing duplicates from a standard list"""
    assert deleteDuplicates([1, 2, 3, 2, 4, 1, 5]) == [1, 2, 3, 4, 5]

def test_delete_duplicates_order_preservation():
    """Ensure the order of first occurrence is maintained"""
    assert deleteDuplicates([3, 1, 2, 3, 1, 4, 2, 5]) == [3, 1, 2, 4, 5]

def test_delete_duplicates_empty_list():
    """Test behavior with an empty list"""
    assert deleteDuplicates([]) == []

def test_delete_duplicates_all_same():
    """Test list with all identical elements"""
    assert deleteDuplicates([1, 1, 1, 1]) == [1]

def test_delete_duplicates_no_duplicates():
    """Test list with no duplicates"""
    assert deleteDuplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_delete_duplicates_type_checking():
    """Ensure the function works with different types of comparable elements"""
    assert deleteDuplicates([1, '1', 2, '2', 1, '1']) == [1, '1', 2, '2']