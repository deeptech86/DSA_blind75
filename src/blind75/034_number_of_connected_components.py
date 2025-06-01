"""
Problem: Number of Connected Components in Undirected Graph
Technique: Union Find, BFS/DFS on Graph
"""

def number_of_connected_components(n, edges):
    """
    You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
    Return the number of connected components in the graph.
    
    Args:
        n: int - Number of nodes
        edges: List[List[int]] - List of edges
        
    Returns:
        int - Number of connected components
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
# Output: 2
# Explanation: There are two connected components: [0, 1, 2] and [3, 4]

# Example 2
# Input: n = 5, edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
# Output: 1
# Explanation: There is one connected component: [0, 1, 2, 3, 4]
