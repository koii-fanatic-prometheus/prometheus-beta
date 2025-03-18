import pytest
import random
import typing
from src.sort_performance_logger import log_sorting_performance

def bubble_sort(arr: list) -> list:
    """Simple bubble sort implementation for testing."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr: list) -> list:
    """Quick sort implementation for testing."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def test_log_sorting_performance_basic():
    """Test basic functionality of performance logger."""
    def generate_random_list():
        return [random.randint(1, 1000) for _ in range(100)]
    
    results = log_sorting_performance(
        bubble_sort, 
        sorted, 
        generate_random_list,
        num_trials=5
    )
    
    # Check result structure
    assert "algorithm1" in results
    assert "algorithm2" in results
    assert results["num_trials"] == 5
    
    # Check algorithm details
    assert results["algorithm1"]["name"] == "bubble_sort"
    assert results["algorithm2"]["name"] == "sorted"
    
    # Check times
    assert len(results["algorithm1"]["times"]) == 5
    assert len(results["algorithm2"]["times"]) == 5
    assert "avg_time" in results["algorithm1"]
    assert "avg_time" in results["algorithm2"]

def test_log_sorting_performance_edge_cases():
    """Test edge cases and error handling."""
    def generate_empty_list():
        return []
    
    def generate_single_element_list():
        return [42]
    
    # Empty list
    results_empty = log_sorting_performance(
        bubble_sort, 
        sorted, 
        generate_empty_list,
        num_trials=3
    )
    assert results_empty["num_trials"] == 3
    
    # Single element list
    results_single = log_sorting_performance(
        bubble_sort, 
        sorted, 
        generate_single_element_list,
        num_trials=3
    )
    assert results_single["num_trials"] == 3
    
    # Invalid inputs
    with pytest.raises(ValueError, match="Both sorting algorithms must be callable"):
        log_sorting_performance(
            "not a function", 
            sorted, 
            generate_empty_list
        )
    
    with pytest.raises(ValueError, match="Number of trials must be at least 1"):
        log_sorting_performance(
            bubble_sort, 
            sorted, 
            generate_empty_list,
            num_trials=0
        )

def test_log_sorting_performance_different_algorithms():
    """Test performance logging with different sorting algorithms."""
    def generate_random_list():
        return [random.randint(1, 1000) for _ in range(200)]
    
    results = log_sorting_performance(
        bubble_sort, 
        quick_sort, 
        generate_random_list,
        num_trials=5
    )
    
    # Verify sorting consistency
    # This test will raise an exception if algorithms produce different results
    log_sorting_performance(
        bubble_sort, 
        sorted, 
        generate_random_list,
        num_trials=5
    )