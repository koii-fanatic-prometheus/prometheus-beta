def min_coins(coins, amount):
    """
    Find the minimum number of coins needed to make a given amount of change.
    
    Args:
        coins (list): A list of coin denominations available.
        amount (int): The target amount to make change for.
    
    Returns:
        int: Minimum number of coins needed to make the amount, 
             or -1 if the amount cannot be made with given coins.
    
    Raises:
        ValueError: If coins list is empty or contains non-positive values.
        TypeError: If inputs are not of the correct type.
    """
    # Input validation
    if not isinstance(coins, list):
        raise TypeError("Coins must be a list of integers")
    
    if not coins:
        raise ValueError("Coins list cannot be empty")
    
    # Check for invalid coin denominations 
    if any(not isinstance(coin, int) or coin <= 0 for coin in coins):
        raise ValueError("All coins must be positive integers")
    
    if not isinstance(amount, int):
        raise TypeError("Amount must be an integer")
    
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    
    # Special case: if amount is 0, no coins needed
    if amount == 0:
        return 0
    
    # Dynamic programming solution 
    # dp[i] will store the minimum coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    # Compute minimum coins for each amount from 1 to target amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    # Return result or -1 if amount cannot be made
    return dp[amount] if dp[amount] != float('inf') else -1