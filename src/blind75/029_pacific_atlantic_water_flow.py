"""
Problem: Pacific Atlantic Water Flow
Technique: Matrix as Graph, BFS/DFS
"""

def pacific_atlantic_water_flow(heights):
    """
    Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent,
    the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
    Water can flow in four directions (up, down, left, or right) from one cell to another one with height equal or lower.
    Find the list of grid coordinates where water can flow to both the Pacific and Atlantic oceans.
    
    Args:
        heights: List[List[int]] - Matrix of heights
        
    Returns:
        List[List[int]] - List of grid coordinates
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: heights = [
#   [1, 2, 2, 3, 5],
#   [3, 2, 3, 4, 4],
#   [2, 4, 5, 3, 1],
#   [6, 7, 1, 4, 5],
#   [5, 1, 1, 2, 4]
# ]
# Output: [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
# Explanation: These points can flow to both the Pacific and Atlantic oceans

# Example 2
# Input: heights = [
#   [2, 1],
#   [1, 2]
# ]
# Output: [[0, 0], [0, 1], [1, 0], [1, 1]]
# Explanation: All cells can flow to both oceans
