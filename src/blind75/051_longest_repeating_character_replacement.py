"""
Problem: Longest Repeating Character Replacement
Technique: Sliding Window (Flexible Longest)
"""

def longest_repeating_character_replacement(s, k):
    """
    Given a string s and an integer k, you can choose any character of the string and change it to any other uppercase English character.
    You can perform this operation at most k times.
    Return the length of the longest substring containing the same letter you can get after performing the above operations.
    
    Args:
        s: str - Input string
        k: int - Maximum number of operations
        
    Returns:
        int - Length of the longest substring containing the same letter
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

# Example 2
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with 'B's or the two 'B's with 'A's to form "AAAA" or "BBBB"
