import pytest
from src.coin_change import min_coins

def test_basic_coin_change():
    """Test basic coin change scenarios"""
    assert min_coins([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert min_coins([2], 3) == -1  # Cannot make 3 with only 2-cent coins
    assert min_coins([1], 100) == 100  # Can always make amount with 1-cent coins

def test_zero_amount():
    """Test when target amount is zero"""
    assert min_coins([1, 2, 5], 0) == 0

def test_single_coin_denomination():
    """Test scenarios with a single coin denomination"""
    assert min_coins([1], 5) == 5
    assert min_coins([2], 6) == 3
    assert min_coins([5], 7) == -1

def test_multiple_coin_denominations():
    """Test various coin denomination scenarios"""
    assert min_coins([1, 3, 4], 6) == 2  # 3 + 3 or 4 + 2
    assert min_coins([2, 3, 5], 8) == 2  # 3 + 5
    assert min_coins([2, 5, 10, 20], 15) == 2  # 5 + 10

def test_error_handling():
    """Test error cases"""
    with pytest.raises(TypeError, match="Coins must be a list of integers"):
        min_coins("not a list", 10)
    
    with pytest.raises(ValueError, match="Coins list cannot be empty"):
        min_coins([], 10)
    
    with pytest.raises(ValueError, match="All coins must be positive integers"):
        min_coins([1, 0, -2], 10)
    
    with pytest.raises(TypeError, match="Amount must be an integer"):
        min_coins([1, 2, 5], "10")
    
    with pytest.raises(ValueError, match="Amount cannot be negative"):
        min_coins([1, 2, 5], -10)

def test_edge_cases():
    """Test edge cases"""
    assert min_coins([2], 1) == -1  # Impossible to make
    assert min_coins([1, 2, 5], 100) == 20  # Large amount
    assert min_coins([186, 419, 83, 408], 6249) == 20  # Complex scenario