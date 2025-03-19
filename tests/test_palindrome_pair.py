import pytest
from src.palindrome_pair import palindrome_pair, is_palindrome

def test_is_palindrome():
    """Test the is_palindrome helper function."""
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(11) == True
    assert is_palindrome(0) == True

def test_palindrome_pair_basic_positive():
    """Test cases with existing palindrome difference pairs."""
    assert palindrome_pair([11, 12, 13, 22]) == True  # 22 - 11 = 11 (palindrome)
    assert palindrome_pair([10, 20, 30, 44]) == True  # 44 - 10 = 34 (palindrome)

def test_palindrome_pair_basic_negative():
    """Test cases without palindrome difference pairs."""
    assert palindrome_pair([1, 3, 5, 7]) == False
    assert palindrome_pair([2, 4, 6, 8]) == False

def test_palindrome_pair_edge_cases():
    """Test edge cases."""
    assert palindrome_pair([]) == False  # Empty list
    assert palindrome_pair([5]) == False  # Single element
    assert palindrome_pair([11, 22, 33]) == True  # Multiple palindrome possibilities

def test_palindrome_pair_invalid_input():
    """Test invalid input handling."""
    with pytest.raises(TypeError):
        palindrome_pair("not a list")
    
    with pytest.raises(ValueError):
        palindrome_pair([1, 2, "3", 4])

def test_palindrome_pair_negative_numbers():
    """Test with negative numbers and mixed number types."""
    assert palindrome_pair([-11, 0, 11]) == True  # 11 - (-11) = 22 (palindrome)
    assert palindrome_pair([-1, 0, 1]) == True  # 1 - 0 = 1 (palindrome)

def test_palindrome_pair_large_numbers():
    """Test with larger numbers."""
    assert palindrome_pair([100, 111, 222, 333]) == True  # 333 - 111 = 222 (palindrome)
    assert palindrome_pair([1000, 2000, 3000]) == False

def test_print_differences():
    """Diagnostic test to print all differences."""
    nums = [1, 3, 5, 7]
    differences = [abs(nums[j] - nums[i]) for i in range(len(nums)) for j in range(i+1, len(nums))]
    print("\nAll differences:", differences)
    palindrome_differences = [diff for diff in differences if is_palindrome(diff)]
    print("Palindrome differences:", palindrome_differences)