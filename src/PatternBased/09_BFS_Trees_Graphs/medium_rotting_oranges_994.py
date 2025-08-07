"""
LeetCode 994: Rotting Oranges
Difficulty: Medium
Pattern: BFS - Graphs

You are given an m x n grid where each cell can have one of three values:
- 0 representing an empty cell,
- 1 representing a fresh orange, or
- 2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

Example:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 10
- grid[i][j] is 0, 1, or 2.
"""

def orangesRotting(grid):
    """
    Time Complexity: O(m * n)
    Space Complexity: O(m * n)
    
    TODO: Implement the solution using BFS multi-source traversal
    Hint: Start BFS from all initially rotten oranges simultaneously, track time elapsed
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [[2,1,1],[1,1,0],[0,1,1]],
        [[2,1,1],[0,1,1],[1,0,1]],
        [[0,2]],
        [[1]]
    ]
    
    for grid in test_cases:
        # Create a copy for testing since we modify the grid
        grid_copy = [row[:] for row in grid]
        result = orangesRotting(grid_copy)
        print(f"Grid:")
        for row in grid:
            print(row)
        print(f"Minutes: {result}\n")
