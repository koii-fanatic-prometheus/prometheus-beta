import pytest
from src.unique_grid_paths import find_shortest_path

def test_simple_path():
    """Test a simple grid with a clear path"""
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 4

def test_no_path():
    """Test a grid with no possible path"""
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert find_shortest_path(grid) is None

def test_single_cell():
    """Test a single-cell grid"""
    grid = [[0]]
    assert find_shortest_path(grid) == 1

def test_single_cell_blocked():
    """Test a single-cell blocked grid"""
    grid = [[1]]
    assert find_shortest_path(grid) is None

def test_constrained_path():
    """Test a grid with complex movement constraints"""
    grid = [
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 1, 0]
    ]
    assert find_shortest_path(grid) == 6

def test_empty_grid():
    """Test an empty grid"""
    grid = []
    assert find_shortest_path(grid) is None

def test_non_square_grid():
    """Test a non-square grid"""
    grid = [
        [0, 0],
        [0, 0],
        [0, 0]
    ]
    assert find_shortest_path(grid) is None  # As per implementation, requires square grid

def test_only_down_movement():
    """Test a grid where only downward movement is possible"""
    grid = [
        [0, 1, 1],
        [0, 1, 1],
        [0, 0, 0]
    ]
    assert find_shortest_path(grid) == 3