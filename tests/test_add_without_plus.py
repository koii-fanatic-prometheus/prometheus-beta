import pytest
from src.add_without_plus import add_without_plus

def test_basic_addition():
    """Test basic addition with positive numbers"""
    assert add_without_plus(2, 3) == 5
    assert add_without_plus(10, 20) == 30
    assert add_without_plus(0, 5) == 5
    assert add_without_plus(5, 0) == 5

def test_negative_numbers():
    """Test addition with negative numbers"""
    assert add_without_plus(-2, 3) == 1
    assert add_without_plus(2, -3) == -1
    assert add_without_plus(-5, -7) == -12

def test_zero_addition():
    """Test addition with zero"""
    assert add_without_plus(0, 0) == 0

def test_large_numbers():
    """Test addition with larger numbers"""
    assert add_without_plus(1000, 2000) == 3000
    assert add_without_plus(-1000, 1000) == 0

def test_invalid_input():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        add_without_plus("2", 3)
    with pytest.raises(TypeError):
        add_without_plus(2, "3")
    with pytest.raises(TypeError):
        add_without_plus(2.5, 3)

def test_symmetric_addition():
    """Test that addition is symmetric"""
    assert add_without_plus(5, 7) == add_without_plus(7, 5)