import pytest
from src.mountain_range import create_mountain_range, Peak

def test_create_mountain_range_basic():
    """Test basic functionality of creating a mountain range"""
    peaks = create_mountain_range(5)
    
    # Check correct number of peaks
    assert len(peaks) == 5
    
    # Check each peak is a Peak instance
    assert all(isinstance(peak, Peak) for peak in peaks)

def test_create_mountain_range_height_range():
    """Test that peaks are generated within specified height range"""
    min_height = 2000.0
    max_height = 5000.0
    peaks = create_mountain_range(10, min_height=min_height, max_height=max_height)
    
    # Check all peaks are within height range
    assert all(min_height <= peak.height <= max_height for peak in peaks)

def test_create_mountain_range_name_prefix():
    """Test that name prefix works correctly"""
    prefix = "Himalayan"
    peaks = create_mountain_range(3, name_prefix=prefix)
    
    # Check peak names start with prefix
    assert all(peak.name.startswith(prefix) for peak in peaks)

def test_create_mountain_range_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Test zero peaks
    with pytest.raises(ValueError, match="Number of peaks must be at least 1"):
        create_mountain_range(0)
    
    # Test negative peaks
    with pytest.raises(ValueError, match="Number of peaks must be at least 1"):
        create_mountain_range(-3)
    
    # Test invalid height range
    with pytest.raises(ValueError, match="Minimum height must be less than or equal to maximum height"):
        create_mountain_range(5, min_height=8000, max_height=5000)

def test_create_mountain_range_coordinates():
    """Test that latitude and longitude are within valid ranges"""
    peaks = create_mountain_range(10)
    
    # Check latitude range (-90 to 90)
    assert all(-90 <= peak.latitude <= 90 for peak in peaks)
    
    # Check longitude range (-180 to 180)
    assert all(-180 <= peak.longitude <= 180 for peak in peaks)

def test_peak_uniqueness():
    """Test that generated peaks have unique names"""
    peaks_without_prefix = create_mountain_range(5)
    peak_names = [peak.name for peak in peaks_without_prefix]
    assert len(set(peak_names)) == len(peak_names)
    
    peaks_with_prefix = create_mountain_range(5, name_prefix="Alps")
    peak_names = [peak.name for peak in peaks_with_prefix]
    assert len(set(peak_names)) == len(peak_names)