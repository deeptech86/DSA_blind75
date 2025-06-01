"""
Problem: Construct Binary Tree from Preorder and Inorder Traversal
Technique: DFS on Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def construct_binary_tree_from_preorder_and_inorder_traversal(preorder, inorder):
    """
    Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
    and inorder is the inorder traversal of the same tree, construct and return the binary tree.
    
    Args:
        preorder: List[int] - Preorder traversal
        inorder: List[int] - Inorder traversal
        
    Returns:
        TreeNode - Root of the constructed binary tree
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
# Output: [3, 9, 20, None, None, 15, 7]
#      3
#     / \
#    9  20
#      /  \
#     15   7
# Explanation: The tree is constructed from the preorder and inorder traversals

# Example 2
# Input: preorder = [1, 2], inorder = [2, 1]
# Output: [1, 2]
#    1
#   /
#  2
# Explanation: The tree is constructed from the preorder and inorder traversals
