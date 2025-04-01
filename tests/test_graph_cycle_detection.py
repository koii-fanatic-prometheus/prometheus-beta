import pytest
from src.graph_cycle_detection import detect_cycle_in_directed_graph

def test_graph_with_no_cycle():
    graph = {
        0: [1, 2],
        1: [2],
        2: [3],
        3: []
    }
    assert detect_cycle_in_directed_graph(graph) == False

def test_graph_with_cycle():
    graph = {
        0: [1],
        1: [2],
        2: [0],
        3: [4]
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_graph_with_multiple_cycles():
    graph = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: [4],
        4: [2]
    }
    assert detect_cycle_in_directed_graph(graph) == True

def test_empty_graph():
    graph = {}
    assert detect_cycle_in_directed_graph(graph) == False

def test_single_node_graph():
    graph = {0: []}
    assert detect_cycle_in_directed_graph(graph) == False

def test_single_node_cycle_graph():
    graph = {0: [0]}
    assert detect_cycle_in_directed_graph(graph) == True

def test_invalid_graph_none():
    with pytest.raises(ValueError, match="Graph cannot be None"):
        detect_cycle_in_directed_graph(None)

def test_invalid_graph_type():
    with pytest.raises(ValueError, match="Graph must be a dictionary"):
        detect_cycle_in_directed_graph([1, 2, 3])

def test_graph_with_disconnected_components():
    graph = {
        0: [1],
        1: [2],
        2: [],
        3: [4],
        4: [5],
        5: [3]
    }
    assert detect_cycle_in_directed_graph(graph) == True