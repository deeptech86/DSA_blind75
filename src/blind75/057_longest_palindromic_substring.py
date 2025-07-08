"""
Problem: Longest Palindromic Substring
Technique: Two Pointers, Dynamic Programming
"""

def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring in s.
    
    Args:
        s: str - Input string
        
    Returns:
        str - Longest palindromic substring
    """
    # TODO: Implement solution
    left=0
    right=len(s)
    lst= list(str)
    while left < right:
        if lst[left] != lst[right]:
            right = right-1





# Example 1
# Input: s = "babad"
# Output: "bab" or "aba"
# Explanation: Both "bab" and "aba" are valid longest palindromic substrings

# Example 2
# Input: s = "cbbd"
# Output: "bb"
# Explanation: "bb" is the longest palindromic substring
