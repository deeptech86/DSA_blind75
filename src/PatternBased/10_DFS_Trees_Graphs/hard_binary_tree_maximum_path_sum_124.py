"""
LeetCode 124: Binary Tree Maximum Path Sum
Difficulty: Hard
Pattern: DFS - Trees

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes 
in the sequence has an edge connecting them. A node can only appear in the sequence 
at most once. The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example:
Input: root = [1,2,3]
Output: 6 (The optimal path is 2 -> 1 -> 3 with path sum 2 + 1 + 3 = 6)

Constraints:
- The number of nodes in the tree is in the range [1, 3 * 10^4].
- -1000 <= Node.val <= 1000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    """
    Time Complexity: O(n)
    Space Complexity: O(h) where h is height of tree
    
    TODO: Implement the solution using DFS with path sum tracking
    Hint: For each node, calculate max path through that node, update global max
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
        [1, 2, 3],
        [-10, 9, 20, None, None, 15, 7],
        [-3],
        [2, -1]
    ]
    
    for values in test_cases:
        root = create_tree(values)
        result = maxPathSum(root)
        print(f"Input: {values}")
        print(f"Maximum path sum: {result}\n")
