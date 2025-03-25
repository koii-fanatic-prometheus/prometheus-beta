import pytest
from src.fibonacci_memoized import fibonacci_memoized

def test_fibonacci_base_cases():
    """Test base cases of Fibonacci sequence"""
    assert fibonacci_memoized(0) == 0
    assert fibonacci_memoized(1) == 1

def test_fibonacci_known_values():
    """Test known Fibonacci sequence values"""
    assert fibonacci_memoized(2) == 1
    assert fibonacci_memoized(3) == 2
    assert fibonacci_memoized(4) == 3
    assert fibonacci_memoized(5) == 5
    assert fibonacci_memoized(6) == 8
    assert fibonacci_memoized(10) == 55

def test_larger_fibonacci_numbers():
    """Test larger Fibonacci numbers to ensure memoization works efficiently"""
    assert fibonacci_memoized(20) == 6765
    assert fibonacci_memoized(30) == 832040

def test_negative_input_raises_error():
    """Ensure negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        fibonacci_memoized(-1)

def test_non_integer_input_raises_error():
    """Ensure non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_memoized(3.14)
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_memoized("10")
    with pytest.raises(TypeError, match="Input must be an integer"):
        fibonacci_memoized([])