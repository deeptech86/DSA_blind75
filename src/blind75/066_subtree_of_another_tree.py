"""
Problem: Subtree of Another Tree
Technique: DFS on Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def subtree_of_another_tree(root, subRoot):
    """
    Given the roots of two binary trees root and subRoot,
    return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
    
    Args:
        root: TreeNode - Root of the main tree
        subRoot: TreeNode - Root of the subtree
        
    Returns:
        bool - True if subRoot is a subtree of root, False otherwise
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: root = [3, 4, 5, 1, 2], subRoot = [4, 1, 2]
#        3
#       / \
#      4   5
#     / \
#    1   2
#
#     4
#    / \
#   1   2
# Output: True
# Explanation: The tree rooted at 4 is a subtree of the main tree

# Example 2
# Input: root = [3, 4, 5, 1, 2, None, None, None, None, 0], subRoot = [4, 1, 2]
#        3
#       / \
#      4   5
#     / \
#    1   2
#       /
#      0
#
#     4
#    / \
#   1   2
# Output: False
# Explanation: The tree rooted at 4 is not a subtree of the main tree
