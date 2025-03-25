import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from knights_tour import KnightsTour

def test_knights_tour_initialization():
    """Test the initialization of KnightsTour"""
    kt = KnightsTour()
    assert kt.board_size == 8
    assert len(kt.moves) == 8

def test_invalid_start_position():
    """Test handling of invalid start positions"""
    kt = KnightsTour()
    
    # Test outside board boundaries
    with pytest.raises(ValueError, match="Start position is outside the board"):
        kt.solve(-1, 0)
    
    with pytest.raises(ValueError, match="Start position is outside the board"):
        kt.solve(8, 8)

def test_knights_tour_solution():
    """Test that a Knight's Tour solution is found"""
    kt = KnightsTour()
    
    # Test a few different start positions
    start_positions = [
        (0, 0),   # Top-left corner
        (3, 3),   # Center-ish
        (7, 7),   # Bottom-right corner
    ]
    
    for start_x, start_y in start_positions:
        solution = kt.solve(start_x, start_y)
        
        # Solution should not be None
        assert solution is not None, f"No solution found for start position ({start_x}, {start_y})"
        
        # Check solution properties
        flat_solution = [cell for row in solution for cell in row]
        
        # Verify all squares are visited exactly once
        assert len(set(flat_solution)) == kt.board_size * kt.board_size
        assert len(flat_solution) == kt.board_size * kt.board_size
        assert min(flat_solution) == 0
        assert max(flat_solution) == kt.board_size * kt.board_size - 1

def test_knights_move_validity():
    """Test the is_valid_move method"""
    kt = KnightsTour()
    
    # Prepare a board with some moves
    board = [[-1 for _ in range(8)] for _ in range(8)]
    board[0][0] = 0  # Mark first move
    
    # Valid moves (within board and unvisited)
    assert kt.is_valid_move(board, 1, 2)
    assert kt.is_valid_move(board, 2, 1)
    
    # Invalid moves
    board[1][2] = 1  # Mark a previously tested move
    assert not kt.is_valid_move(board, 1, 2)  # Already visited
    assert not kt.is_valid_move(board, 8, 8)  # Outside board