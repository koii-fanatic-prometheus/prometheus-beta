def find_two_sum_indices(nums, target):
    """
    Find two indices in the given array that add up to the target sum.

    Args:
        nums (list): A list of integers to search through.
        target (int): The target sum to find.

    Returns:
        list: A list containing two indices [index1, index2] where 
              nums[index1] + nums[index2] == target. 
              Returns an empty list if no such indices exist.

    Raises:
        TypeError: If input is not a list or target is not an integer.
        ValueError: If input list contains non-numeric elements.
    """
    # Type checking
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    if not isinstance(target, (int, float)):
        raise TypeError("Target must be a numeric value")
    
    # Check for non-numeric elements
    if any(not isinstance(x, (int, float)) for x in nums):
        raise ValueError("List must contain only numeric elements")
    
    # Use a hash map for O(n) time complexity
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # If complement exists in the map, we found our pair
        if complement in num_map:
            return [num_map[complement], i]
        
        # Add current number and its index to the map
        num_map[num] = i
    
    # If no solution is found
    return []