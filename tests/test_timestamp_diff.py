import pytest
from src.timestamp_diff import calculate_timestamp_difference

def test_timestamp_difference_same_time():
    result = calculate_timestamp_difference('2023-01-01 12:00:00', '2023-01-01 12:00:00')
    assert result == 0

def test_timestamp_difference_one_hour():
    result = calculate_timestamp_difference('2023-01-01 12:00:00', '2023-01-01 13:00:00')
    assert result == 3600  # 1 hour = 3600 seconds

def test_timestamp_difference_negative_order():
    result = calculate_timestamp_difference('2023-01-01 13:00:00', '2023-01-01 12:00:00')
    assert result == 3600  # Order shouldn't matter

def test_custom_timestamp_format():
    result = calculate_timestamp_difference('01/01/2023 12:00:00', '01/01/2023 13:00:00', 
                                            format='%m/%d/%Y %H:%M:%S')
    assert result == 3600

def test_invalid_timestamp_format():
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        calculate_timestamp_difference('invalid', 'format')

def test_different_date_difference():
    result = calculate_timestamp_difference('2023-01-01 00:00:00', '2023-01-02 00:00:00')
    assert result == 86400  # 1 day = 86400 seconds