import pytest
from src.dijkstra_shortest_path import dijkstra_shortest_path, reconstruct_path

def test_simple_graph():
    # Simple graph with known shortest paths
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    # Test distances from node A
    distances, previous = dijkstra_shortest_path(graph, 'A')
    
    assert distances == {
        'A': 0,
        'B': 3,  # A -> C -> B
        'C': 2,  # A -> C
        'D': 6   # A -> C -> B -> D
    }
    
    # Test path reconstruction
    path = reconstruct_path(previous, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']

def test_disconnected_node():
    graph = {
        'A': {'B': 4},
        'B': {'A': 4},
        'C': {}  # Completely disconnected
    }
    
    distances, previous = dijkstra_shortest_path(graph, 'A')
    
    assert distances['C'] == float('inf')
    assert previous['C'] is None

def test_start_node_validation():
    graph = {
        'A': {'B': 4},
        'B': {'A': 4}
    }
    
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        dijkstra_shortest_path(graph, 'X')

def test_path_reconstruction_no_path():
    graph = {
        'A': {'B': 4},
        'B': {'A': 4},
        'C': {'D': 1},
        'D': {'C': 1}
    }
    
    distances, previous = dijkstra_shortest_path(graph, 'A')
    
    with pytest.raises(ValueError, match="No path exists between A and C"):
        reconstruct_path(previous, 'A', 'C')

def test_weighted_graph():
    graph = {
        'start': {'A': 5, 'B': 2},
        'A': {'C': 4, 'D': 2},
        'B': {'A': 8, 'D': 7},
        'C': {'D': 6, 'end': 3},
        'D': {'end': 1},
        'end': {}
    }
    
    distances, previous = dijkstra_shortest_path(graph, 'start')
    
    # Verify shortest distance to 'end'
    assert distances['end'] == 8  # start -> B -> D -> end
    
    # Path reconstruction
    path = reconstruct_path(previous, 'start', 'end')
    
    # Verify total path length and start/end points
    assert len(path) == 4
    assert path[0] == 'start'
    assert path[-1] == 'end'
    
    # Verify total distance matches
    total_distance = sum(
        graph[path[i]][path[i+1]] 
        for i in range(len(path)-1)
    )
    assert total_distance == 8

def test_self_loop_handling():
    graph = {
        'A': {'A': 1, 'B': 3},
        'B': {'C': 2},
        'C': {}
    }
    
    distances, previous = dijkstra_shortest_path(graph, 'A')
    
    assert distances['C'] == 5  # A -> B -> C
    assert previous['C'] == 'B'