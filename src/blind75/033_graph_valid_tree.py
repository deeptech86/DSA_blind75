"""
Problem: Graph Valid Tree
Technique: Union Find, BFS/DFS on Graph
"""

def graph_valid_tree(n, edges):
    """
    You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
    Return true if the edges of the given graph make up a valid tree, and false otherwise.
    
    Args:
        n: int - Number of nodes
        edges: List[List[int]] - List of edges
        
    Returns:
        bool - True if the graph is a valid tree, False otherwise
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: n = 5, edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
# Output: True
# Explanation: The graph is a valid tree with 5 nodes and 4 edges

# Example 2
# Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
# Output: False
# Explanation: The graph has a cycle: [1, 2, 3, 1], so it's not a tree
