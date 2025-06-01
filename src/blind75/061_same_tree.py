"""
Problem: Same Tree
Technique: DFS on Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def same_tree(p, q):
    """
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.
    
    Args:
        p: TreeNode - Root of the first tree
        q: TreeNode - Root of the second tree
        
    Returns:
        bool - True if the trees are the same, False otherwise
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: p = [1, 2, 3], q = [1, 2, 3]
#     1       1
#    / \     / \
#   2   3   2   3
# Output: True
# Explanation: The trees are identical in structure and values

# Example 2
# Input: p = [1, 2], q = [1, None, 2]
#    1      1
#   /        \
#  2          2
# Output: False
# Explanation: The trees are different in structure
