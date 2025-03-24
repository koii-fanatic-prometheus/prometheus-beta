import pytest
from datetime import datetime, timedelta
from src.add_days_to_date import add_days_to_date

def test_add_positive_days_string_input():
    """Test adding positive days with string input"""
    result = add_days_to_date('2023-01-01', 5)
    assert result == datetime(2023, 1, 6)

def test_add_positive_days_datetime_input():
    """Test adding positive days with datetime input"""
    date = datetime(2023, 1, 1)
    result = add_days_to_date(date, 5)
    assert result == datetime(2023, 1, 6)

def test_add_negative_days():
    """Test adding negative days (going back in time)"""
    result = add_days_to_date('2023-01-10', -3)
    assert result == datetime(2023, 1, 7)

def test_handle_year_change():
    """Test adding days that cross year boundary"""
    result = add_days_to_date('2022-12-30', 3)
    assert result == datetime(2023, 1, 2)

def test_invalid_date_format():
    """Test raising error for invalid date format"""
    with pytest.raises(ValueError, match="Invalid date format"):
        add_days_to_date('01-01-2023', 5)

def test_invalid_days_type():
    """Test raising error for non-integer days"""
    with pytest.raises(TypeError, match="Days must be an integer"):
        add_days_to_date('2023-01-01', '5')

def test_invalid_date_type():
    """Test raising error for invalid date type"""
    with pytest.raises(TypeError, match="Date must be a string"):
        add_days_to_date(20230101, 5)

def test_leap_year():
    """Test handling of leap year dates"""
    result = add_days_to_date('2024-02-28', 1)
    assert result == datetime(2024, 2, 29)

def test_large_day_addition():
    """Test adding a large number of days"""
    result = add_days_to_date('2023-01-01', 365)
    assert result == datetime(2024, 1, 1)