def count_staircase_combinations(stair_lengths):
    """
    Calculate the number of ways to climb a staircase with given stair lengths.
    
    The climber can take 1 or 2 steps at a time.
    
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
    
    # Total height of the staircase
    total_height = sum(stair_lengths)
    
    # Dynamic programming to count combinations
    # dp[i] represents the number of ways to reach height i
    dp = [0] * (total_height + 1)
    
    # Base cases
    dp[0] = 1  # One way to reach height 0 (starting point)
    
    # Iterate through possible heights
    for height in range(1, total_height + 1):
        # Can climb 1 or 2 steps, if the steps are valid
        if height >= 1:
            dp[height] += dp[height - 1]
        if height >= 2:
            dp[height] += dp[height - 2]
    
    return dp[total_height]