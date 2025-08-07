"""
LeetCode 76: Minimum Window Substring
Difficulty: Hard
Pattern: Sliding Window (Longest Variable Window)

Given two strings s and t of lengths m and n respectively, return the minimum window 
substring of s such that every character in t (including duplicates) is included in 
the window. If there is no such window in s that covers all characters in t, return 
the empty string "".

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Constraints:
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""

def minWindow(s, t):
    """
    Time Complexity: O(|s| + |t|)
    Space Complexity: O(|s| + |t|)
    
    TODO: Implement the solution using sliding window technique
    Hint: Use two pointers, expand right until valid window, then contract left to minimize
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("ADOBECODEBANC", "ABC"),
        ("a", "a"),
        ("a", "aa"),
        ("ab", "b")
    ]
    
    for s, t in test_cases:
        result = minWindow(s, t)
        print(f's: "{s}", t: "{t}"')
        print(f'Minimum window: "{result}"\n')
