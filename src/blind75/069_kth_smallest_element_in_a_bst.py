"""
Problem: Kth Smallest Element in a BST
Technique: Binary Search Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest_element_in_a_bst(root, k):
    """
    Given the root of a binary search tree, and an integer k,
    return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
    
    Args:
        root: TreeNode - Root of the BST
        k: int - The k-th smallest value to find
        
    Returns:
        int - The k-th smallest value in the BST
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: root = [3, 1, 4, None, 2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# Output: 1
# Explanation: The 1st smallest element in the BST is 1

# Example 2
# Input: root = [5, 3, 6, 2, 4, None, None, 1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# Output: 3
# Explanation: The 3rd smallest element in the BST is 3
