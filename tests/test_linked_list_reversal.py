import pytest
from src.linked_list_reversal import LinkedList, Node, create_linked_list

def test_node_creation():
    """Test Node class initialization."""
    node = Node(5)
    assert node.value == 5
    assert node.next is None

def test_linked_list_creation():
    """Test creating a linked list."""
    ll = create_linked_list(5)
    assert ll.to_list() == [1, 2, 3, 4, 5]

def test_linked_list_reverse():
    """Test reversing a linked list."""
    ll = create_linked_list(5)
    ll.reverse()
    assert ll.to_list() == [5, 4, 3, 2, 1]

def test_empty_list_reverse():
    """Test reversing an empty list."""
    ll = LinkedList()
    ll.reverse()
    assert ll.to_list() == []

def test_single_node_reverse():
    """Test reversing a list with a single node."""
    ll = LinkedList()
    ll.append(1)
    ll.reverse()
    assert ll.to_list() == [1]

def test_create_linked_list_negative_input():
    """Test creating a linked list with negative input."""
    with pytest.raises(ValueError, match="Number of nodes must be non-negative"):
        create_linked_list(-1)

def test_linked_list_append():
    """Test appending nodes to a linked list."""
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    assert ll.to_list() == [1, 2, 3]