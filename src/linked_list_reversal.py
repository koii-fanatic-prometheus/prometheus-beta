class Node:
    """
    Represents a node in a linked list.
    
    Attributes:
        value (int): The value stored in the node.
        next (Node, optional): Reference to the next node in the list. Defaults to None.
    """
    def __init__(self, value):
        """
        Initialize a new Node.
        
        Args:
            value (int): The value to be stored in the node.
        """
        self.value = value
        self.next = None

class LinkedList:
    """
    Represents a linked list with methods to create, append, and reverse.
    """
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
    
    def append(self, value):
        """
        Append a new node with the given value to the end of the list.
        
        Args:
            value (int): The value to be added to the list.
        """
        new_node = Node(value)
        
        # If the list is empty, set the new node as head
        if not self.head:
            self.head = new_node
            return
        
        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        
        # Append the new node
        current.next = new_node
    
    def reverse(self):
        """
        Reverse the order of nodes in the linked list.
        
        Returns:
            LinkedList: The reversed linked list.
        """
        # Handle empty list or single node list
        if not self.head or not self.head.next:
            return self
        
        # Reverse the links
        prev = None
        current = self.head
        
        while current:
            # Store the next node before changing links
            next_node = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move pointers forward
            prev = current
            current = next_node
        
        # Update the head to the last node (now first)
        self.head = prev
        
        return self
    
    def to_list(self):
        """
        Convert the linked list to a Python list for easy comparison.
        
        Returns:
            list: A list of node values in order.
        """
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

def create_linked_list(n):
    """
    Create a linked list with n nodes, where each node's value is its position.
    
    Args:
        n (int): Number of nodes to create.
    
    Returns:
        LinkedList: A linked list with n nodes.
    
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Number of nodes must be non-negative")
    
    linked_list = LinkedList()
    for i in range(1, n + 1):
        linked_list.append(i)
    
    return linked_list