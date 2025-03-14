import pytest
from src.one_char_deletion import can_convert_by_one_deletion

def test_valid_one_char_deletion():
    """Test basic valid one-character deletion scenarios"""
    assert can_convert_by_one_deletion("abcd", "abc") == True
    assert can_convert_by_one_deletion("abcd", "abd") == True
    assert can_convert_by_one_deletion("abcd", "acd") == True
    assert can_convert_by_one_deletion("abcd", "bcd") == True

def test_invalid_conversions():
    """Test scenarios where conversion is not possible"""
    assert can_convert_by_one_deletion("abcd", "abcde") == False
    assert can_convert_by_one_deletion("abc", "def") == False
    assert can_convert_by_one_deletion("abcd", "abc1") == False

def test_edge_cases():
    """Test edge cases"""
    assert can_convert_by_one_deletion("a", "") == True
    assert can_convert_by_one_deletion("", "") == False
    assert can_convert_by_one_deletion("", "a") == False

def test_type_and_input_handling():
    """Test error handling and type constraints"""
    with pytest.raises(TypeError):
        can_convert_by_one_deletion(123, "abc")
    with pytest.raises(TypeError):
        can_convert_by_one_deletion("abc", 123)