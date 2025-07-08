"""
Problem: Valid Anagram
Technique: Hash Table
"""

def valid_anagram(s, t):
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    
    Args:
        s: str - First string
        t: str - Second string
        
    Returns:
        bool - True if t is an anagram of s, False otherwise
    """
    # TODO: Implement solution
    if len(s)==len(t):
        for char in s:
            if s.count(char)== t.count(char):
                return True
    else:
        return False


# Example 1
# Input: s = "anagram", t = "nagaram"
# Output: True
# Explanation: The characters in s can be rearranged to form t

# Example 2
# Input: s = "rat", t = "car"
# Output: False
# Explanation: The characters in s cannot be rearranged to form t

s = "anagram"
t = "nagaram"
print(valid_anagram(s, t))