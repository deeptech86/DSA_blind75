"""
Problem: Serialize and Deserialize Binary Tree
Technique: DFS/BFS on Tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        Args:
            root: TreeNode - Root of the binary tree
            
        Returns:
            str - Serialized string
        """
        # TODO: Implement solution
        pass
        
    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        Args:
            data: str - Serialized string
            
        Returns:
            TreeNode - Root of the deserialized binary tree
        """
        # TODO: Implement solution
        pass


# Example 1
# Input: root = [1, 2, 3, None, None, 4, 5]
#      1
#     / \
#    2   3
#       / \
#      4   5
# Output: [1, 2, 3, None, None, 4, 5]
# Explanation: Serializing the tree and then deserializing should return the original tree

# Example 2
# Input: root = []
# Output: []
# Explanation: Serializing an empty tree and then deserializing should return an empty tree
