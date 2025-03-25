import heapq
from typing import Dict, List, Tuple, Optional

def dijkstra_shortest_path(graph: Dict[str, Dict[str, int]], start: str) -> Tuple[Dict[str, int], Dict[str, Optional[str]]]:
    """
    Implement Dijkstra's algorithm to find shortest paths from a start node.
    
    Args:
        graph (Dict[str, Dict[str, int]]): Adjacency list representation of the graph.
                                           Keys are nodes, values are dictionaries of 
                                           neighboring nodes and their edge weights.
        start (str): Starting node for path calculation.
    
    Returns:
        Tuple containing:
        - Dict of shortest distances from start to each node
        - Dict of previous nodes in the shortest path
    
    Raises:
        ValueError: If start node is not in the graph
    """
    # Validate input
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")
    
    # Initialize distances and previous nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {node: None for node in graph}
    
    # Priority queue to store nodes to visit
    pq = [(0, start)]
    
    # Track visited nodes to prevent redundant processing
    visited = set()
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if node already processed
        if current_node in visited:
            continue
        visited.add(current_node)
        
        # If we've found a longer path, skip
        if current_distance > distances[current_node]:
            continue
        
        # Check all neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # Update if shorter path found or equal distance with different route
            if (distance < distances[neighbor]) or \
               (distance == distances[neighbor] and current_node < previous[neighbor]):
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous

def reconstruct_path(previous: Dict[str, Optional[str]], start: str, end: str) -> List[str]:
    """
    Reconstruct the shortest path between start and end nodes.
    
    Args:
        previous (Dict[str, Optional[str]]): Dictionary of previous nodes in shortest paths
        start (str): Starting node
        end (str): Destination node
    
    Returns:
        List of nodes forming the shortest path
    
    Raises:
        ValueError: If path between start and end cannot be found
    """
    # Check if a path exists
    if previous[end] is None and end != start:
        raise ValueError(f"No path exists between {start} and {end}")
    
    path = []
    current = end
    
    while current is not None:
        path.append(current)
        current = previous[current]
        
        # Break to avoid infinite loop
        if current is None:
            break
    
    # Reverse to get path from start to end
    return list(reversed(path))