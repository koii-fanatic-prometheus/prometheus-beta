import pytest
from src.array_xor import find_array_xor

def test_array_xor_basic():
    """Test XOR of basic integer arrays."""
    assert find_array_xor([1, 2, 3]) == 0  # 1 ^ 2 ^ 3 = 0
    assert find_array_xor([5, 3, 7]) == 1  # 5 ^ 3 ^ 7 = 1
    assert find_array_xor([10]) == 10  # Single element case

def test_array_xor_with_zero():
    """Test XOR with zero elements."""
    assert find_array_xor([0, 1, 2]) == 3  # 0 ^ 1 ^ 2 = 3
    assert find_array_xor([0, 0, 0]) == 0  # Multiple zeros

def test_array_xor_error_handling():
    """Test error handling for invalid inputs."""
    # Empty list should raise ValueError
    with pytest.raises(ValueError, match="Cannot calculate XOR of an empty list"):
        find_array_xor([])
    
    # Non-list input should raise TypeError
    with pytest.raises(TypeError, match="Input must be a list"):
        find_array_xor(42)
    
    # Non-integer elements should raise TypeError
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_array_xor([1, 2, "3"])
    with pytest.raises(TypeError, match="All elements must be integers"):
        find_array_xor([1.5, 2, 3])

def test_array_xor_large_numbers():
    """Test XOR with larger numbers."""
    assert find_array_xor([1024, 2048, 4096]) == 7168  # 1024 ^ 2048 ^ 4096 = 7168
    assert find_array_xor([10**6, 10**6 + 1, 10**6 + 2]) == 3  # Large numbers