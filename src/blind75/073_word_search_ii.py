"""
Problem: Word Search II
Technique: Trie, Matrix as Graph, DFS with Backtracking
"""

def word_search_ii(board, words):
    """
    Given an m x n board of characters and a list of strings words, return all words on the board.
    Each word must be constructed from letters of sequentially adjacent cells,
    where adjacent cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once in a word.
    
    Args:
        board: List[List[str]] - Board of characters
        words: List[str] - List of words to search for
        
    Returns:
        List[str] - List of words found on the board
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: board = [
#   ['o', 'a', 'a', 'n'],
#   ['e', 't', 'a', 'e'],
#   ['i', 'h', 'k', 'r'],
#   ['i', 'f', 'l', 'v']
# ], words = ["oath", "pea", "eat", "rain"]
# Output: ["eat", "oath"]
# Explanation: The words "oath" and "eat" can be found in the board

# Example 2
# Input: board = [
#   ['a', 'b'],
#   ['c', 'd']
# ], words = ["abcb"]
# Output: []
# Explanation: The word "abcb" cannot be found in the board
