import pytest
from src.cocktail_shaker_sort import cocktail_shaker_sort

def test_cocktail_shaker_sort_normal_list():
    """Test sorting a normal list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert cocktail_shaker_sort(input_list) == expected

def test_cocktail_shaker_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert cocktail_shaker_sort(input_list) == input_list

def test_cocktail_shaker_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert cocktail_shaker_sort(input_list) == expected

def test_cocktail_shaker_sort_empty_list():
    """Test sorting an empty list."""
    assert cocktail_shaker_sort([]) == []

def test_cocktail_shaker_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert cocktail_shaker_sort(input_list) == input_list

def test_cocktail_shaker_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert cocktail_shaker_sort(input_list) == expected

def test_cocktail_shaker_sort_float_list():
    """Test sorting a list of floats."""
    input_list = [3.14, 2.71, 1.41, 0.58, 2.23]
    expected = sorted(input_list)
    assert cocktail_shaker_sort(input_list) == expected

def test_cocktail_shaker_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 3, -2, 0, 1, -9]
    expected = sorted(input_list)
    assert cocktail_shaker_sort(input_list) == expected

def test_cocktail_shaker_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        cocktail_shaker_sort("not a list")

def test_cocktail_shaker_sort_uncomparable_elements():
    """Test that a TypeError is raised for incomparable elements."""
    with pytest.raises(TypeError, match="List contains elements that cannot be compared"):
        cocktail_shaker_sort([1, "a", 3])