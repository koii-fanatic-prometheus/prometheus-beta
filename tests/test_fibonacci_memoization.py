import pytest
from src.fibonacci_memoization import fibonacci_memoized

def test_basic_fibonacci_numbers():
    """Test basic Fibonacci sequence numbers."""
    assert fibonacci_memoized(0) == 0
    assert fibonacci_memoized(1) == 1
    assert fibonacci_memoized(2) == 1
    assert fibonacci_memoized(3) == 2
    assert fibonacci_memoized(5) == 5
    assert fibonacci_memoized(10) == 55

def test_larger_fibonacci_numbers():
    """Test larger Fibonacci numbers to validate memoization performance."""
    assert fibonacci_memoized(20) == 6765
    assert fibonacci_memoized(30) == 832040

def test_negative_input():
    """Test handling of negative inputs."""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_memoized(-1)
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_memoized(-100)

def test_non_integer_input():
    """Test handling of non-integer inputs."""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_memoized(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_memoized("5")
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_memoized(None)