"""
Problem: Lowest Common Ancestor of BST
Technique: Binary Search Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor_of_bst(root, p, q):
    """
    Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
    
    Args:
        root: TreeNode - Root of the BST
        p: TreeNode - First node
        q: TreeNode - Second node
        
    Returns:
        TreeNode - Lowest common ancestor node
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p = 2, q = 8
#         6
#       /   \
#      2     8
#     / \   / \
#    0   4 7   9
#       / \
#      3   5
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6

# Example 2
# Input: root = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5], p = 2, q = 4
#         6
#       /   \
#      2     8
#     / \   / \
#    0   4 7   9
#       / \
#      3   5
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2
