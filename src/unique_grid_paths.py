from typing import List, Optional

def find_shortest_path(grid: List[List[int]]) -> Optional[int]:
    """
    Find the shortest path from top-left to bottom-right in a grid with movement constraints.
    
    Movement constraints:
    - Can move right or down
    - Can only move to an empty cell (0)
    - Must move down if right is blocked
    
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
    
    # If start or end is blocked, no path is possible
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return None
    
    # Dynamic Programming solution with strict movement constraints
    # dp[i][j] represents the shortest path to cell (i,j)
    dp = [[float('inf')] * n for _ in range(n)]
    dp[0][0] = 1
    
    # Initialize first row (can only move right if previous cell is accessible)
    for j in range(1, n):
        if grid[0][j] == 0 and grid[0][j-1] == 0:
            dp[0][j] = dp[0][j-1] + 1
    
    # Initialize first column (can only move down)
    for i in range(1, n):
        if grid[i][0] == 0 and grid[i-1][0] == 0:
            dp[i][0] = dp[i-1][0] + 1
    
    # Fill the DP table
    for i in range(1, n):
        for j in range(1, n):
            # Skip blocked cells
            if grid[i][j] == 1:
                continue
            
            # Try to move from left (right move)
            if grid[i][j-1] == 0:
                dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
            
            # Always try moving from top (down move)
            if grid[i-1][j] == 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
    
    # Return shortest path or None if no path exists
    return dp[n-1][n-1] if dp[n-1][n-1] != float('inf') else None