import pytest
from src.timestamp_difference import calculate_timestamp_difference

def test_basic_timestamp_difference():
    """Test calculating difference between two timestamps"""
    result = calculate_timestamp_difference(
        '2023-01-01 10:00:00', 
        '2023-01-01 11:00:00'
    )
    assert result == 3600  # 1 hour = 3600 seconds

def test_negative_time_difference():
    """Test when first timestamp is later than second"""
    result = calculate_timestamp_difference(
        '2023-01-01 12:00:00', 
        '2023-01-01 11:00:00'
    )
    assert result == -3600  # -1 hour = -3600 seconds

def test_custom_format():
    """Test with a different timestamp format"""
    result = calculate_timestamp_difference(
        '01/01/2023 10:00:00', 
        '01/01/2023 11:00:00', 
        format='%m/%d/%Y %H:%M:%S'
    )
    assert result == 3600  # 1 hour = 3600 seconds

def test_invalid_timestamp_format():
    """Test handling of invalid timestamp format"""
    with pytest.raises(ValueError, match="Error parsing timestamps"):
        calculate_timestamp_difference(
            'invalid-timestamp', 
            '2023-01-01 11:00:00'
        )

def test_different_day_difference():
    """Test difference across multiple days"""
    result = calculate_timestamp_difference(
        '2023-01-01 00:00:00', 
        '2023-01-02 00:00:00'
    )
    assert result == 86400  # 1 day = 86400 seconds

def test_same_timestamp():
    """Test when both timestamps are identical"""
    result = calculate_timestamp_difference(
        '2023-01-01 10:00:00', 
        '2023-01-01 10:00:00'
    )
    assert result == 0  # No time difference