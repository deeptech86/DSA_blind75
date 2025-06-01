"""
Problem: Word Search
Technique: Matrix as Graph, DFS with Backtracking
"""

def word_search(board, word):
    """
    Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cells,
    where adjacent cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once.
    
    Args:
        board: List[List[str]] - Grid of characters
        word: str - Word to search for
        
    Returns:
        bool - True if word exists in the grid, False otherwise
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: board = [
#   ['A', 'B', 'C', 'E'],
#   ['S', 'F', 'C', 'S'],
#   ['A', 'D', 'E', 'E']
# ], word = "ABCCED"
# Output: True
# Explanation: The word "ABCCED" can be found by starting at the top-left A and following the path A→B→C→C→E→D

# Example 2
# Input: board = [
#   ['A', 'B', 'C', 'E'],
#   ['S', 'F', 'C', 'S'],
#   ['A', 'D', 'E', 'E']
# ], word = "SEE"
# Output: True
# Explanation: The word "SEE" can be found by starting at the middle S and following the path S→E→E
