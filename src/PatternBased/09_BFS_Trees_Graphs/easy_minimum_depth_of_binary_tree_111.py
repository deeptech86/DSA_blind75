"""
LeetCode 111: Minimum Depth of Binary Tree
Difficulty: Easy
Pattern: BFS - Trees

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root 
node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Constraints:
- The number of nodes in the tree is in the range [0, 10^5].
- -1000 <= Node.val <= 1000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root):
    """
    Time Complexity: O(n)
    Space Complexity: O(w) where w is maximum width
    
    TODO: Implement the solution using BFS traversal
    Hint: Use level-order traversal, return depth when first leaf node is encountered
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
        [2, None, 3, None, 4, None, 5, None, 6],
        [1],
        []
    ]
    
    for values in test_cases:
        root = create_tree(values)
        result = minDepth(root)
        print(f"Input: {values}")
        print(f"Minimum depth: {result}\n")
