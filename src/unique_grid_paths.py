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
    
    # Depth-first search with path length tracking
    def dfs(x: int, y: int, visited: set, current_path: List[tuple]) -> Optional[int]:
        # Out of bounds or blocked cell
        if (x < 0 or x >= n or y < 0 or y >= n or 
            grid[x][y] == 1 or (x, y) in visited):
            return None
        
        # Reached destination
        if x == n-1 and y == n-1:
            return len(current_path)
        
        # Mark current cell as visited
        visited.add((x, y))
        
        # Try moving right first (if possible)
        if y+1 < n and grid[x][y+1] == 0:
            right_path = dfs(x, y+1, visited.copy(), current_path + [(x, y+1)])
        else:
            right_path = None
        
        # If right is blocked, try moving down
        down_path = dfs(x+1, y, visited.copy(), current_path + [(x+1, y)])
        
        # Return the shortest valid path
        if right_path is not None and down_path is not None:
            return min(right_path, down_path)
        elif right_path is not None:
            return right_path
        elif down_path is not None:
            return down_path
        
        return None
    
    # Start DFS from top-left
    result = dfs(0, 0, set(), [(0, 0)])
    return result