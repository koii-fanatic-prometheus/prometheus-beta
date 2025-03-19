def find_pair_with_target(nums, target):
    """
    Find index pairs of numbers that sum up to the target in a list of unique integers.

    Args:
        nums (list): A list of unique integers.
        target (int): The target sum to find.

    Returns:
        list: A list of index pairs where the numbers at those indices sum to the target.
               Returns an empty list if no such pairs exist.

    Raises:
        TypeError: If inputs are not of the expected types.
        ValueError: If nums is empty.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Input validation
    if not isinstance(nums, list):
        raise TypeError("Input 'nums' must be a list")
    if not isinstance(target, int):
        raise TypeError("Input 'target' must be an integer")
    
    # Check for empty list
    if not nums:
        raise ValueError("Input list cannot be empty")
    
    # Use a hash map to store complements
    complement_map = {}
    result = []
    
    # Iterate through the list
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists and ensure specific index ordering
        if complement in complement_map:
            # Check each index of the complement
            for j in complement_map[complement]:
                # Specific ordering requirements
                pair = tuple(sorted([j, i]))
                if pair not in result:
                    result.append(pair)
        
        # Add current index to the list of indices for this number
        if num not in complement_map:
            complement_map[num] = []
        complement_map[num].append(i)
    
    # Return sorted pairs
    return sorted(result)