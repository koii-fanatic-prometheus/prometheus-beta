import pytest
from src.list_union import find_list_union

def test_basic_list_union():
    """Test basic list union with unique and overlapping elements."""
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    assert find_list_union(list1, list2) == [1, 2, 3, 4, 5]

def test_list_union_with_duplicates():
    """Test list union with duplicate elements."""
    list1 = [1, 2, 2, 3]
    list2 = [3, 4, 4, 5]
    assert find_list_union(list1, list2) == [1, 2, 3, 4, 5]

def test_list_union_order_preservation():
    """Test that the union preserves the order of first occurrence."""
    list1 = [5, 3, 1]
    list2 = [2, 4, 1]
    assert find_list_union(list1, list2) == [5, 3, 1, 2, 4]

def test_list_union_empty_lists():
    """Test union of empty lists."""
    list1 = []
    list2 = []
    assert find_list_union(list1, list2) == []

def test_list_union_one_empty_list():
    """Test union when one list is empty."""
    list1 = [1, 2, 3]
    list2 = []
    assert find_list_union(list1, list2) == [1, 2, 3]

def test_list_union_mixed_types():
    """Test union with mixed type elements."""
    list1 = [1, 'a', 2, 'b']
    list2 = ['b', 3, 'c', 1]
    assert find_list_union(list1, list2) == [1, 'a', 2, 'b', 3, 'c']

def test_list_union_invalid_input_type():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Both arguments must be lists"):
        find_list_union("not a list", [1, 2, 3])
    
    with pytest.raises(TypeError, match="Both arguments must be lists"):
        find_list_union([1, 2, 3], "not a list")
    
    with pytest.raises(TypeError, match="Both arguments must be lists"):
        find_list_union(None, [1, 2, 3])