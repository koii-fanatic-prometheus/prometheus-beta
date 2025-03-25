import pytest
from src.prime_factors import find_prime_factors

def test_prime_factors_basic():
    """Test basic prime factorization"""
    assert find_prime_factors(12) == [2, 2, 3]
    assert find_prime_factors(15) == [3, 5]
    assert find_prime_factors(100) == [2, 2, 5, 5]

def test_prime_factors_prime_number():
    """Test prime numbers return themselves"""
    assert find_prime_factors(7) == [7]
    assert find_prime_factors(11) == [11]
    assert find_prime_factors(17) == [17]

def test_prime_factors_one():
    """Test edge case of 1"""
    assert find_prime_factors(1) == []

def test_prime_factors_large_number():
    """Test a larger number with multiple prime factors"""
    assert find_prime_factors(84) == [2, 2, 3, 7]

def test_prime_factors_invalid_input():
    """Test invalid input raises ValueError"""
    with pytest.raises(ValueError):
        find_prime_factors(0)
    
    with pytest.raises(ValueError):
        find_prime_factors(-5)
    
    with pytest.raises(ValueError):
        find_prime_factors(3.14)
    
    with pytest.raises(ValueError):
        find_prime_factors("not a number")