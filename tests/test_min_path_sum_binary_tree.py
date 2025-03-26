import pytest
from src.min_path_sum_binary_tree import TreeNode, min_path_sum

def test_min_path_sum_basic():
    """Test basic binary tree with multiple nodes"""
    # Tree structure:
    #       10
    #      /  \
    #     5    15
    #    / \
    #   2   8
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(8)
    
    assert min_path_sum(root) == 15  # Minimum path: 10 -> 5 -> 2

def test_min_path_sum_single_node():
    """Test tree with only a root node"""
    root = TreeNode(5)
    assert min_path_sum(root) == 5

def test_min_path_sum_empty_tree():
    """Test empty tree"""
    assert min_path_sum(None) is None

def test_min_path_sum_unbalanced_tree():
    """Test unbalanced tree"""
    # Tree structure:
    #       10
    #      /
    #     5
    #    /
    #   2
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(2)
    
    assert min_path_sum(root) == 17  # 10 -> 5 -> 2

def test_min_path_sum_complex_tree():
    """Test a more complex tree"""
    # Tree structure:
    #         20
    #       /    \
    #     8       22
    #    / \
    #   4   12
    #      /  \
    #     10   14
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(12)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)
    
    assert min_path_sum(root) == 38  # 20 -> 8 -> 4

def test_min_path_sum_invalid_input():
    """Test invalid input raises TypeError"""
    with pytest.raises(TypeError):
        min_path_sum("not a tree")
    with pytest.raises(TypeError):
        min_path_sum(5)
    with pytest.raises(TypeError):
        min_path_sum([1, 2, 3])