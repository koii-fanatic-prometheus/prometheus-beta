import pytest
from src.recursive_gcd import recursive_gcd

def test_gcd_basic_cases():
    """Test basic GCD calculations."""
    assert recursive_gcd(48, 18) == 6
    assert recursive_gcd(54, 24) == 6
    assert recursive_gcd(17, 23) == 1

def test_gcd_zero():
    """Test cases involving zero."""
    assert recursive_gcd(0, 5) == 5
    assert recursive_gcd(5, 0) == 5
    assert recursive_gcd(0, 0) == 0

def test_gcd_negative_inputs():
    """Test that function works with negative inputs."""
    assert recursive_gcd(-48, 18) == 6
    assert recursive_gcd(48, -18) == 6
    assert recursive_gcd(-48, -18) == 6

def test_gcd_same_number():
    """Test GCD of a number with itself."""
    assert recursive_gcd(7, 7) == 7
    assert recursive_gcd(100, 100) == 100

def test_gcd_one():
    """Test GCD of coprime numbers."""
    assert recursive_gcd(17, 23) == 1
    assert recursive_gcd(5, 7) == 1

def test_invalid_input_types():
    """Test that invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        recursive_gcd(5.5, 10)
    with pytest.raises(TypeError):
        recursive_gcd("10", 20)
    with pytest.raises(TypeError):
        recursive_gcd([10], 20)