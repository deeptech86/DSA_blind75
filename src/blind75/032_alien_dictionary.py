"""
Problem: Alien Dictionary
Technique: Directed Graph / Topological Sort
"""

def alien_dictionary(words):
    """
    There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.
    You are given a list of strings words from the alien language's dictionary, where the strings in words are sorted lexicographically by the rules of this new language.
    Return a string of the unique letters in the new alien language sorted in lexicographically increasing order by the new language's rules.
    If there is no solution, return "". If there are multiple solutions, return any of them.
    
    Args:
        words: List[str] - List of words sorted in the alien language
        
    Returns:
        str - Unique letters sorted in lexicographically increasing order
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: words = ["wrt", "wrf", "er", "ett", "rftt"]
# Output: "wertf"
# Explanation: The correct order is: w, e, r, t, f

# Example 2
# Input: words = ["z", "x"]
# Output: "zx"
# Explanation: The correct order is: z, x
