import pytest
from src.tower_of_hanoi import tower_of_hanoi, print_tower_of_hanoi_moves
import io
import sys

def test_tower_of_hanoi_zero_disks():
    """Test solving Tower of Hanoi with zero disks"""
    assert tower_of_hanoi(0) == []

def test_tower_of_hanoi_one_disk():
    """Test solving Tower of Hanoi with one disk"""
    moves = tower_of_hanoi(1)
    assert moves == [('A', 'C')]
    assert len(moves) == 1

def test_tower_of_hanoi_three_disks():
    """Test solving Tower of Hanoi with three disks"""
    moves = tower_of_hanoi(3)
    expected_moves_count = 2**3 - 1  # 2^n - 1 moves for n disks
    assert len(moves) == expected_moves_count
    
    # Check logical correctness
    assert moves[0] == ('A', 'C')
    assert moves[1] == ('A', 'B')

def test_tower_of_hanoi_custom_rods():
    """Test solving Tower of Hanoi with custom rod names"""
    moves = tower_of_hanoi(2, 'X', 'Y', 'Z')
    assert moves[0] == ('X', 'Y')
    assert moves[1] == ('X', 'Z')
    assert moves[2] == ('Y', 'Z')

def test_tower_of_hanoi_invalid_input():
    """Test handling of invalid input"""
    with pytest.raises(ValueError):
        tower_of_hanoi(-1)
    
    with pytest.raises(ValueError):
        tower_of_hanoi(1.5)

def test_print_tower_of_hanoi_moves():
    """Test printing moves to console"""
    # Capture console output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Call the print function with small number of disks
    print_tower_of_hanoi_moves(2)
    
    # Restore stdout
    sys.stdout = sys.__stdout__
    
    # Check output
    output = captured_output.getvalue().strip().split('\n')
    assert len(output) == 3  # 2^2 - 1 moves
    assert all('Move disk from' in move for move in output)

def test_tower_of_hanoi_seven_disks():
    """Test solving Tower of Hanoi with specified 7 disks"""
    moves = tower_of_hanoi(7)
    expected_moves_count = 2**7 - 1  # 2^n - 1 moves for n disks
    assert len(moves) == expected_moves_count