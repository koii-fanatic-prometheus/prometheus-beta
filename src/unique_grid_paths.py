from typing import List, Optional

def find_shortest_path(grid: List[List[int]]) -> Optional[int]:
    """
    Find the shortest path from top-left to bottom-right in a grid with movement constraints.
    
    Movement constraints:
    - Can only move right or down
    - Can only move to an empty cell (0)
    - If right is blocked, must move down
    
    Args:
        grid (List[List[int]]): N x N grid of 0s and 1s
    
    Returns:
        Optional[int]: Length of the shortest path, or None if no path exists
    """
    # Validate input
    if not grid or not grid[0]:
        return None
    
    # Validate square grid
    n = len(grid)
    if any(len(row) != n for row in grid):
        return None
    
    # Create a DP table to store path lengths
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Initialize starting point
    if grid[0][0] == 1:
        return None
    dp[0][0] = 1
    
    # Fill the first row
    for j in range(1, n):
        # Can only move right if current and previous cells are empty
        if grid[0][j] == 0:
            dp[0][j] = dp[0][j-1] + 1 if grid[0][j-1] == 0 else float('inf')
    
    # Fill the first column
    for i in range(1, n):
        # Can only move down if current and previous cells are empty
        if grid[i][0] == 0:
            dp[i][0] = dp[i-1][0] + 1 if grid[i-1][0] == 0 else float('inf')
    
    # Fill the rest of the DP table
    for i in range(1, n):
        for j in range(1, n):
            # Skip blocked cells
            if grid[i][j] == 1:
                continue
            
            # Possible paths
            up_path = dp[i-1][j] + 1 if grid[i-1][j] == 0 else float('inf')
            left_path = dp[i][j-1] + 1 if grid[i][j-1] == 0 else float('inf')
            
            # Choose the minimum valid path
            dp[i][j] = min(up_path, left_path)
    
    # Return the path length to bottom-right, or None if no path exists
    return dp[n-1][n-1] if dp[n-1][n-1] != float('inf') else None