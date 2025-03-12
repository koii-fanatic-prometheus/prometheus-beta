import random
import dataclasses
from typing import List, Optional

@dataclasses.dataclass
class Peak:
    """
    Represents a mountain peak with its characteristics.
    
    Attributes:
        name (str): Name of the peak
        height (float): Height of the peak in meters
        latitude (float): Latitude coordinate of the peak
        longitude (float): Longitude coordinate of the peak
    """
    name: str
    height: float
    latitude: float
    longitude: float

def create_mountain_range(num_peaks: int, 
                           min_height: float = 1000.0, 
                           max_height: float = 8848.0, 
                           name_prefix: Optional[str] = None) -> List[Peak]:
    """
    Generate a list of mountain peaks for a mountain range.
    
    Args:
        num_peaks (int): Number of peaks to generate
        min_height (float, optional): Minimum height of peaks in meters. Defaults to 1000.0.
        max_height (float, optional): Maximum height of peaks in meters. Defaults to 8848.0 (Everest height).
        name_prefix (str, optional): Prefix for peak names. Defaults to None.
    
    Returns:
        List[Peak]: A list of generated mountain peaks
    
    Raises:
        ValueError: If num_peaks is less than 1
        ValueError: If min_height is greater than max_height
    """
    # Validate inputs
    if num_peaks < 1:
        raise ValueError("Number of peaks must be at least 1")
    
    if min_height > max_height:
        raise ValueError("Minimum height must be less than or equal to maximum height")
    
    # Generate peaks
    peaks = []
    for i in range(num_peaks):
        # Generate unique peak name
        peak_name = f"{name_prefix or 'Peak'} {i+1}" if name_prefix is not None else f"Peak {i+1}"
        
        # Randomly generate height within specified range
        peak_height = random.uniform(min_height, max_height)
        
        # Randomly generate latitude and longitude (roughly covering entire Earth)
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        
        # Create and add peak
        peak = Peak(
            name=peak_name,
            height=round(peak_height, 2),
            latitude=round(latitude, 4),
            longitude=round(longitude, 4)
        )
        peaks.append(peak)
    
    return peaks