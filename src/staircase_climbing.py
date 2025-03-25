def count_staircase_combinations(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given stair lengths.
    
    The climber can take 1 or 2 steps at a time, using the provided stair lengths.
    
    Args:
        stair_lengths (list): A list of integers representing the heights of stairs.
        
    Returns:
        int: The total number of unique ways to climb the staircase.
        
    Raises:
        ValueError: If stair_lengths is empty or contains non-positive values.
    """
    # Validate input
    if not stair_lengths:
        raise ValueError("Stair lengths cannot be empty")
    
    if any(length <= 0 for length in stair_lengths):
        raise ValueError("All stair lengths must be positive integers")
    
    # Preprocess the stair lengths to get the total height
    total_height = sum(stair_lengths)
    
    # Dynamic programming to count combinations
    # dp[i] represents the number of ways to reach height i
    dp = [0] * (total_height + 1)
    
    # Base case
    dp[0] = 1  # One way to reach height 0 (starting point)
    
    # Iterate through the stair lengths to ensure we only use valid steps
    valid_steps = set(stair_lengths)
    
    # Iterate through possible heights
    for height in range(1, total_height + 1):
        # Check each possible step length
        for step in valid_steps:
            # If we can reach this height by taking this step
            if height >= step:
                dp[height] += dp[height - step]
    
    return dp[total_height]