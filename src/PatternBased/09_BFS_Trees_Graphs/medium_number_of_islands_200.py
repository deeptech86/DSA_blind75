"""
LeetCode 200: Number of Islands
Difficulty: Medium
Pattern: BFS - Graphs

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), 
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally 
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 300
- grid[i][j] is '0' or '1'.
"""

def numIslands(grid):
    """
    Time Complexity: O(m * n)
    Space Complexity: O(min(m, n)) for BFS queue
    
    TODO: Implement the solution using BFS traversal
    Hint: For each '1' found, start BFS to mark all connected land cells, then increment island count
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ],
        [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ],
        [
            ["1"]
        ],
        [
            ["0"]
        ]
    ]
    
    for grid in test_cases:
        # Create a copy for testing since we modify the grid
        grid_copy = [row[:] for row in grid]
        result = numIslands(grid_copy)
        print(f"Grid:")
        for row in grid:
            print(row)
        print(f"Number of islands: {result}\n")
