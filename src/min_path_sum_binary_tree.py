class TreeNode:
    """
    A class representing a node in a binary tree.
    
    Attributes:
        val (int): The value stored in the node.
        left (TreeNode): Left child node.
        right (TreeNode): Right child node.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_path_sum(root):
    """
    Find the minimum path sum from root to any leaf in a binary tree.
    
    Args:
        root (TreeNode): The root of the binary tree.
    
    Returns:
        int: The minimum path sum. 
             Returns None if the tree is empty.
             Returns the root's value if it's a leaf node.
    
    Raises:
        TypeError: If root is not a TreeNode or None.
    
    Time Complexity: O(n), where n is the number of nodes in the tree
    Space Complexity: O(h), where h is the height of the tree (recursion stack)
    """
    # Check for invalid input
    if root is None:
        return None
    
    # Validate input type
    if not isinstance(root, TreeNode):
        raise TypeError("Input must be a TreeNode or None")
    
    # If it's a leaf node, return its value
    if root.left is None and root.right is None:
        return root.val
    
    # Recursively find minimum path sum for left and right subtrees
    left_sum = min_path_sum(root.left) if root.left else float('inf')
    right_sum = min_path_sum(root.right) if root.right else float('inf')
    
    # Return the minimum path sum
    return root.val + min(left_sum, right_sum)