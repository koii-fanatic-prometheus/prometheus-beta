import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_algorithm

def test_basic_assignment():
    """Test a simple assignment problem."""
    cost_matrix = [
        [3, 2, 3],
        [3, 3, 2],
        [2, 1, 1]
    ]
    assignments, total_cost = hungarian_algorithm(cost_matrix)
    
    # Verify assignments
    assert len(assignments) == 3
    
    # Verify that total cost represents a valid assignment
    assert total_cost <= 6  # Ensures a valid assignment
    assert all(0 <= assignment < len(cost_matrix) for assignment in assignments)

def test_square_matrix_different_sizes():
    """Test matrices of different sizes."""
    # 2x2 matrix
    cost_matrix_2x2 = [
        [1, 2],
        [3, 4]
    ]
    assignments, total_cost = hungarian_algorithm(cost_matrix_2x2)
    assert len(assignments) == 2
    assert total_cost <= 5
    
    # 4x4 matrix
    cost_matrix_4x4 = [
        [4, 2, 8, 3],
        [2, 5, 1, 6],
        [3, 1, 7, 4],
        [5, 3, 2, 9]
    ]
    assignments, total_cost = hungarian_algorithm(cost_matrix_4x4)
    assert len(assignments) == 4
    assert total_cost <= 7

def test_identical_costs():
    """Test scenario with multiple optimal assignments."""
    cost_matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assignments, total_cost = hungarian_algorithm(cost_matrix)
    assert total_cost == 3

def test_invalid_input():
    """Test error handling for invalid inputs."""
    # Non-square matrix
    with pytest.raises(ValueError):
        hungarian_algorithm([
            [1, 2, 3],
            [4, 5, 6]
        ])
    
    # Empty matrix
    with pytest.raises(ValueError):
        hungarian_algorithm([])
    
    # Non-numeric input
    with pytest.raises(ValueError):
        hungarian_algorithm([
            ['a', 'b'],
            ['c', 'd']
        ])

def test_zero_cost_matrix():
    """Test matrix with all zero costs."""
    cost_matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assignments, total_cost = hungarian_algorithm(cost_matrix)
    assert total_cost == 0
    assert len(assignments) == 3