"""
Problem: Binary Tree Maximum Path Sum
Technique: DFS on Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_maximum_path_sum(root):
    """
    Given a binary tree, find the maximum path sum.
    The path may start and end at any node in the tree.
    
    Args:
        root: TreeNode - Root of the binary tree
        
    Returns:
        int - Maximum path sum
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: root = [1, 2, 3]
#      1
#     / \
#    2   3
# Output: 6
# Explanation: The path with the maximum sum is 1 + 2 + 3 = 6

# Example 2
# Input: root = [-10, 9, 20, None, None, 15, 7]
#      -10
#      / \
#     9  20
#       /  \
#      15   7
# Output: 42
# Explanation: The optimal path is 20 + 15 + 7 = 42
