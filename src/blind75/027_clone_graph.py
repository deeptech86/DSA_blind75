"""
Problem: Clone Graph
Technique: BFS/DFS on Graph
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def clone_graph(node):
    """
    Given a reference of a node in a connected undirected graph,
    return a deep copy (clone) of the graph.
    
    Args:
        node: Node - Reference to a node in the graph
        
    Returns:
        Node - Deep copy of the graph
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: The graph looks like this:
# 1---2
# |   |
# 4---3
# There are no prerequisites to create a deep copy

# Example 2
# Input: adjList = [[1,3],[0,2],[1],[0]]
# Output: [[1,3],[0,2],[1],[0]]
# Explanation: The graph looks like this:
# 0---1
# |   |
# 3   2
