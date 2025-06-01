"""
Problem: Validate Binary Search Tree
Technique: Binary Search Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def validate_binary_search_tree(root):
    """
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).
    
    Args:
        root: TreeNode - Root of the binary tree
        
    Returns:
        bool - True if the tree is a valid BST, False otherwise
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: root = [2, 1, 3]
#    2
#   / \
#  1   3
# Output: True
# Explanation: All nodes satisfy the BST property - left child < node value < right child

# Example 2
# Input: root = [5, 1, 4, None, None, 3, 6]
#     5
#    / \
#   1   4
#      / \
#     3   6
# Output: False
# Explanation: Node value 4 has a right child with value 6, which is greater than the root value 5
