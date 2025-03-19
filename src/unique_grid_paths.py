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
    
    # Breadth-first search to find shortest path
    from collections import deque
    
    # Queue stores: (x, y, path_length)
    queue = deque([(0, 0, 1)])
    visited = set([(0, 0)])
    
    while queue:
        x, y, path_length = queue.popleft()
        
        # Reached destination
        if x == n-1 and y == n-1:
            return path_length
        
        # Try moving right first, if possible
        if y+1 < n and grid[x][y+1] == 0 and (x, y+1) not in visited:
            queue.append((x, y+1, path_length+1))
            visited.add((x, y+1))
        
        # Always try moving down
        if x+1 < n and grid[x+1][y] == 0 and (x+1, y) not in visited:
            queue.append((x+1, y, path_length+1))
            visited.add((x+1, y))
    
    # No path found
    return None