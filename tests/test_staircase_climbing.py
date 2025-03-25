import pytest
from src.staircase_climbing import count_staircase_combinations

def test_basic_staircase():
    """Test a basic staircase with different length steps."""
    assert count_staircase_combinations([1, 1, 1]) == 3
    assert count_staircase_combinations([2, 1]) == 2
    assert count_staircase_combinations([1, 2]) == 2

def test_single_step():
    """Test a staircase with a single step."""
    assert count_staircase_combinations([1]) == 1
    assert count_staircase_combinations([2]) == 1

def test_multiple_steps():
    """Test longer staircases with multiple steps."""
    assert count_staircase_combinations([1, 1, 1, 1]) == 5
    assert count_staircase_combinations([2, 2]) == 2

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Stair lengths cannot be empty"):
        count_staircase_combinations([])
    
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        count_staircase_combinations([0, 1, 2])
    
    with pytest.raises(ValueError, match="All stair lengths must be positive integers"):
        count_staircase_combinations([-1, 1])

def test_large_staircase():
    """Test a larger staircase to ensure performance."""
    large_staircase = [1] * 20
    # This checks that the function can handle more complex scenarios
    result = count_staircase_combinations(large_staircase)
    assert result > 0  # The exact number might be large
    assert isinstance(result, int)