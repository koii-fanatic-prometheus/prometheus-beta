def find_closest_pair_sum(arr, target):
    """
    Find the pair of elements in the array whose sum is closest to the target value.
    
    Args:
        arr (list): Input list of numbers
        target (int/float): Target sum to compare against
    
    Returns:
        tuple: A tuple containing the pair of elements whose sum is closest to the target
        
    Raises:
        ValueError: If the input array has fewer than 2 elements
    """
    # Validate input
    if not arr or len(arr) < 2:
        raise ValueError("Input array must contain at least two elements")
    
    # Initialize variables to track the closest pair
    closest_sum = float('inf')
    closest_pair = None
    
    # Compare all possible pairs
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            current_sum = arr[i] + arr[j]
            current_diff = abs(current_sum - target)
            
            # Update closest pair if:
            # 1. Current sum is closer to target, or
            # 2. Current sum is equally close but occurs first in the original search
            if (current_diff < abs(closest_sum - target) or 
                (current_diff == abs(closest_sum - target) and 
                 (closest_pair is None or (arr[i], arr[j]) < closest_pair))):
                closest_sum = current_sum
                closest_pair = (arr[i], arr[j])
    
    return closest_pair