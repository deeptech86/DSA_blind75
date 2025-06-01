"""
Problem: Decode Ways
Technique: Dynamic Programming (Aggregation and Memoization)
"""

def decode_ways(s):
    """
    A message containing letters from A-Z can be encoded into numbers using the mapping A->1, B->2, ..., Z->26.
    Given a string s containing only digits, return the number of ways to decode it.
    
    Args:
        s: str - String of digits
        
    Returns:
        int - Number of ways to decode the string
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12). There are 2 ways.

# Example 2
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6). There are 3 ways.
