"""
Problem: Maximum Depth of Binary Tree
Technique: DFS on Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maximum_depth_of_binary_tree(root):
    """
    Given the root of a binary tree, return its maximum depth.
    
    Args:
        root: TreeNode - Root of the binary tree
        
    Returns:
        int - Maximum depth of the binary tree
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: root = [3, 9, 20, None, None, 15, 7]
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Output: 3
# Explanation: The maximum depth is 3 (from root to the leaf nodes 15 or 7)

# Example 2
# Input: root = [1, None, 2]
#   1
#    \
#     2
# Output: 2
# Explanation: The maximum depth is 2 (from root to the leaf node 2)
