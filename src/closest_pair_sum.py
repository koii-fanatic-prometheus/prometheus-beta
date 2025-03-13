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
    closest_diff = float('inf')
    closest_pair = None
    
    # Compare all possible pairs
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            current_sum = arr[i] + arr[j]
            current_diff = abs(current_sum - target)
            
            # Update closest pair if:
            # 1. Current sum is closer to target, or
            # 2. Current sum is equally close but occurs first or lexicographically smaller
            if (current_diff < closest_diff or 
                (current_diff == closest_diff and 
                 (closest_pair is None or 
                  (arr[i] < closest_pair[0] or 
                   (arr[i] == closest_pair[0] and arr[j] < closest_pair[1]))))):
                closest_diff = current_diff
                closest_pair = (arr[i], arr[j])
    
    return closest_pair