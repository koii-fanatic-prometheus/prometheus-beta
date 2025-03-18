import pytest
from src.run_length_encoding import run_length_encode, run_length_decode

def test_run_length_encode_basic():
    """Test basic run-length encoding for different input types"""
    # String input
    assert run_length_encode("AABBBCCCC") == [['A', 2], ['B', 3], ['C', 4]]
    
    # List input
    assert run_length_encode(['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C']) == [['A', 2], ['B', 3], ['C', 4]]

def test_run_length_decode_basic():
    """Test basic run-length decoding"""
    # Decode to list or string-like representation
    assert run_length_decode([['A', 2], ['B', 3], ['C', 4]]) == ['A', 'A', 'B', 'B', 'B', 'C', 'C', 'C', 'C']

def test_run_length_encode_edge_cases():
    """Test edge cases for encoding"""
    # Single character
    assert run_length_encode("A") == [['A', 1]]
    
    # Mixed characters
    input_str = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
    result = run_length_encode(input_str)
    assert result == [['W', 12], ['B', 1], ['W', 12], ['B', 3], ['W', 24], ['B', 1]]

def test_run_length_decode_edge_cases():
    """Test edge cases for decoding"""
    # Single element
    assert run_length_decode([['X', 5]]) == ['X', 'X', 'X', 'X', 'X']

def test_run_length_encode_error_handling():
    """Test error handling for invalid inputs"""
    # Empty input
    with pytest.raises(ValueError):
        run_length_encode("")
    
    # Invalid input type
    with pytest.raises(TypeError):
        run_length_encode(123)

def test_run_length_decode_error_handling():
    """Test error handling for decoding"""
    # Invalid input type
    with pytest.raises(TypeError):
        run_length_decode("invalid")
    
    # Malformed input
    with pytest.raises(ValueError):
        run_length_decode([['A'], ['B', 2]])

def test_round_trip():
    """Test round-trip encoding and decoding"""
    original = "AABBBCCCCDDDDDEEEEE"
    encoded = run_length_encode(original)
    decoded = ''.join(run_length_decode(encoded))
    assert decoded == original