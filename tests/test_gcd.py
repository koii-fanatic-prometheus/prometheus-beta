import pytest
from src.gcd import calculate_gcd

def test_gcd_basic_cases():
    """Test basic GCD calculations"""
    assert calculate_gcd(48, 18) == 6
    assert calculate_gcd(54, 24) == 6
    assert calculate_gcd(17, 23) == 1  # Coprime numbers

def test_gcd_same_number():
    """Test GCD when both numbers are the same"""
    assert calculate_gcd(5, 5) == 5
    assert calculate_gcd(100, 100) == 100

def test_gcd_one_is_multiple():
    """Test GCD when one number is a multiple of the other"""
    assert calculate_gcd(12, 36) == 12
    assert calculate_gcd(7, 49) == 7

def test_gcd_input_validation():
    """Test input validation"""
    # Test non-positive inputs
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_gcd(0, 5)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_gcd(5, 0)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_gcd(-5, 10)

def test_gcd_type_validation():
    """Test type validation"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_gcd(3.5, 10)
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_gcd("10", 20)
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_gcd([10], 20)