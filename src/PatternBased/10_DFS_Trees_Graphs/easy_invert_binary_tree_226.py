"""
LeetCode 226: Invert Binary Tree
Difficulty: Easy
Pattern: DFS - Trees

Given the root of a binary tree, invert the tree, and return its root.

Example:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Constraints:
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    """
    Time Complexity: O(n)
    Space Complexity: O(h) where h is height of tree
    
    TODO: Implement the solution using DFS (recursive approach)
    Hint: Recursively swap left and right children for each node
    """
    pass

# Helper functions
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

def tree_to_list(root):
    """Helper function to convert tree back to list for output"""
    if not root:
        return []
    
    from collections import deque
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

# Test cases
if __name__ == "__main__":
    test_cases = [
        [4, 2, 7, 1, 3, 6, 9],
        [2, 1, 3],
        [],
        [1]
    ]
    
    for values in test_cases:
        root = create_tree(values)
        inverted_root = invertTree(root)
        result = tree_to_list(inverted_root)
        print(f"Input: {values}")
        print(f"Inverted: {result}\n")
