def count_subarrays_less_than_k(nums, k):
    """
    Calculate the count of subarrays with product less than k.
    
    Args:
        nums (list): Input list of integers
        k (int): Maximum product threshold
    
    Returns:
        int: Total number of subarrays with product less than k
    
    Raises:
        ValueError: If k is not a positive integer
    """
    # Validate input
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer")
    
    if not nums:
        return 0
    
    # Use sliding window technique
    count = 0
    left = 0
    curr_product = 1
    
    for right in range(len(nums)):
        # Expand the window
        curr_product *= nums[right]
        
        # Shrink window if product exceeds k
        while curr_product >= k and left <= right:
            curr_product //= nums[left]
            left += 1
        
        # Add number of valid subarrays ending at right index
        count += right - left + 1
    
    return count