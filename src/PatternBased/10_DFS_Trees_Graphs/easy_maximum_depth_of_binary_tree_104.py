"""
LeetCode 104: Maximum Depth of Binary Tree
Difficulty: Easy
Pattern: DFS - Trees

Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- -100 <= Node.val <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    """
    Time Complexity: O(n)
    Space Complexity: O(h) where h is height of tree
    
    TODO: Implement the solution using DFS (recursive approach)
    Hint: Base case is when root is None, recursive case adds 1 to max of left and right subtree depths
    """
    pass

# Helper function to create tree from list
def create_tree(values):
    """Helper function to create test cases"""
    if not values:
        return None
    
    from collections import deque
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root

# Test cases
if __name__ == "__main__":
    test_cases = [
        [3, 9, 20, None, None, 15, 7],
        [1, None, 2],
        [],
        [1, 2, 3, 4, 5]
    ]
    
    for values in test_cases:
        root = create_tree(values)
        result = maxDepth(root)
        print(f"Input: {values}")
        print(f"Max depth: {result}\n")
