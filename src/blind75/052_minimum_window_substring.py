"""
Problem: Minimum Window Substring
Technique: Sliding Window (Flexible Shortest)
"""

def minimum_window_substring(s, t):
    """
    Given two strings s and t of lengths m and n respectively, return the minimum window substring of s
    such that every character in t (including duplicates) is included in the window.
    If there is no such substring, return the empty string "".
    
    Args:
        s: str - String to search in
        t: str - Target string
        
    Returns:
        str - Minimum window substring
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t

# Example 2
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window
