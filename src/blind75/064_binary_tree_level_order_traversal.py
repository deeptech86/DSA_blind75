"""
Problem: Binary Tree Level Order Traversal
Technique: BFS on Tree
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_level_order_traversal(root):
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).
    
    Args:
        root: TreeNode - Root of the binary tree
        
    Returns:
        List[List[int]] - Level order traversal
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: root = [3, 9, 20, None, None, 15, 7]
#      3
#     / \
#    9  20
#      /  \
#     15   7
# Output: [[3], [9, 20], [15, 7]]
# Explanation: Level order traversal of the tree

# Example 2
# Input: root = [1]
#     1
# Output: [[1]]
# Explanation: There is only one node at the root level
