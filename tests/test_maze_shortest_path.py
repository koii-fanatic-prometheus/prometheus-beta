import pytest
from src.maze_shortest_path import find_shortest_path

def test_simple_path():
    maze = [
        [' ', ' ', ' '],
        [' ', '#', ' '],
        [' ', ' ', ' ']
    ]
    start = (0, 0)
    end = (2, 2)
    path = find_shortest_path(maze, start, end)
    assert path is not None
    assert len(path) == 5  # Including start and end
    assert path[0] == start
    assert path[-1] == end

def test_blocked_path():
    maze = [
        [' ', '#', ' '],
        ['#', '#', ' '],
        [' ', ' ', ' ']
    ]
    start = (0, 0)
    end = (2, 2)
    path = find_shortest_path(maze, start, end)
    assert path is None  # No path due to complete block

def test_no_path():
    maze = [
        ['#', '#', '#'],
        ['#', '#', '#'],
        ['#', '#', '#']
    ]
    start = (0, 0)
    end = (2, 2)
    path = find_shortest_path(maze, start, end)
    assert path is None

def test_start_is_wall_end():
    maze = [
        [' ', ' ', ' '],
        [' ', '#', ' '],
        [' ', ' ', ' ']
    ]
    start = (1, 1)
    end = (2, 2)
    path = find_shortest_path(maze, start, end)
    assert path is None  # Start is a wall

def test_start_is_end_wall():
    maze = [
        [' ', ' ', ' '],
        [' ', '#', ' '],
        [' ', ' ', ' ']
    ]
    start = (1, 1)
    end = (1, 1)
    path = find_shortest_path(maze, start, end)
    assert path is None  # Start is a wall

def test_start_is_end():
    maze = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    start = (1, 1)
    end = (1, 1)
    path = find_shortest_path(maze, start, end)
    assert path == [(1, 1)]

def test_invalid_start_or_end():
    maze = [
        [' ', ' ', ' '],
        [' ', '#', ' '],
        [' ', ' ', ' ']
    ]
    # Out of bounds
    assert find_shortest_path(maze, (-1, 0), (2, 2)) is None
    assert find_shortest_path(maze, (0, 0), (3, 3)) is None

def test_empty_maze():
    assert find_shortest_path([], (0, 0), (0, 0)) is None
    assert find_shortest_path([[]], (0, 0), (0, 0)) is None

def test_large_maze():
    maze = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', '#', '#', '#', ' '],
        [' ', ' ', ' ', ' ', ' '],
        ['#', '#', '#', '#', ' '],
        [' ', ' ', ' ', ' ', ' ']
    ]
    start = (0, 0)
    end = (4, 4)
    path = find_shortest_path(maze, start, end)
    assert path is not None
    assert len(path) <= 9  # Including start and end
    assert path[0] == start
    assert path[-1] == end