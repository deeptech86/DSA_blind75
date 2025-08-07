"""
LeetCode 98: Validate Binary Search Tree
Difficulty: Medium
Pattern: DFS - Trees

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example:
Input: root = [2,1,3]
Output: true

Constraints:
- The number of nodes in the tree is in the range [1, 10^4].
- -2^31 <= Node.val <= 2^31 - 1
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    """
    Time Complexity: O(n)
    Space Complexity: O(h) where h is height of tree
    
    TODO: Implement the solution using DFS with bounds checking
    Hint: Pass min and max bounds down the tree, check if current node violates bounds
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
        [2, 1, 3],
        [5, 1, 4, None, None, 3, 6],
        [1],
        [10, 5, 15, None, None, 6, 20]
    ]
    
    for values in test_cases:
        root = create_tree(values)
        result = isValidBST(root)
        print(f"Input: {values}")
        print(f"Is valid BST: {result}\n")
