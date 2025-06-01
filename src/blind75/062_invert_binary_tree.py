"""
Problem: Invert/Flip Binary Tree
Technique: DFS on Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(root):
    """
    Given the root of a binary tree, invert the tree, and return its root.
    
    Args:
        root: TreeNode - Root of the binary tree
        
    Returns:
        TreeNode - Root of the inverted binary tree
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: root = [4, 2, 7, 1, 3, 6, 9]
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output: [4, 7, 2, 9, 6, 3, 1]
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Explanation: The tree is inverted by swapping every left and right child

# Example 2
# Input: root = [2, 1, 3]
#   2
#  / \
# 1   3
# Output: [2, 3, 1]
#   2
#  / \
# 3   1
# Explanation: The tree is inverted by swapping every left and right child
