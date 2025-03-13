from typing import List, Tuple, Optional
from collections import deque

def find_shortest_path(maze: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """
    Find the shortest path through a maze from start to end.
    
    Args:
    - maze: A 2D grid representing the maze, where:
        '#' represents walls
        ' ' represents walkable paths
    - start: Starting coordinates (row, col)
    - end: Ending coordinates (row, col)
    
    Returns:
    - A list of coordinates representing the shortest path from start to end
    - None if no path exists
    
    Time Complexity: O(rows * cols)
    Space Complexity: O(rows * cols)
    """
    # Input validation
    if not maze or not maze[0]:
        return None
    
    rows, cols = len(maze), len(maze[0])
    
    # Validate start and end are within maze bounds and not walls
    if (not (0 <= start[0] < rows and 0 <= start[1] < cols) or 
        not (0 <= end[0] < rows and 0 <= end[1] < cols)):
        return None
    
    # Special case: start is end
    if start == end:
        # But check if the cell is a wall or not
        return [start] if maze[start[0]][start[1]] != '#' else None
    
    # Special case: start or end is a wall
    if maze[start[0]][start[1]] == '#' or maze[end[0]][end[1]] == '#':
        return None
    
    # Possible movement directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # Track visited cells to prevent revisiting
    visited = [[False] * cols for _ in range(rows)]
    visited[start[0]][start[1]] = True
    
    # Queue for BFS: (current_pos, path_so_far)
    queue = deque([(start, [start])])
    
    while queue:
        (curr_row, curr_col), path = queue.popleft()
        
        # Check if reached the end
        if (curr_row, curr_col) == end:
            return path
        
        # Explore adjacent cells
        for d_row, d_col in directions:
            next_row, next_col = curr_row + d_row, curr_col + d_col
            
            # Check if next cell is valid: within bounds, not a wall, not visited
            if (0 <= next_row < rows and 
                0 <= next_col < cols and 
                maze[next_row][next_col] != '#' and 
                not visited[next_row][next_col]):
                
                # Mark as visited and add to queue
                visited[next_row][next_col] = True
                new_path = path + [(next_row, next_col)]
                queue.append(((next_row, next_col), new_path))
    
    # No path found
    return None