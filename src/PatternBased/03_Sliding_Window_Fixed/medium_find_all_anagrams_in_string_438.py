"""
LeetCode 438: Find All Anagrams in a String
Difficulty: Medium
Pattern: Sliding Window (Fixed Window)

Given two strings s and p, return an array of all the start indices of p's 
anagrams in s. You may return the answer in any order.

Example:
Input: s = "abab", p = "ab"
Output: [0,2]

Constraints:
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters.
"""

def findAnagrams(s, p):
    """
    Time Complexity: O(n)
    Space Complexity: O(k) where k is the number of unique characters in p
    
    TODO: Implement the solution using sliding window with character counting
    Hint: Use Counter/dictionary to track character frequencies in window
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("abab", "ab"),
        ("abcdefab", "ab"),
        ("cbaebabacd", "abc"),
        ("baa", "aa")
    ]
    
    for s, p in test_cases:
        result = findAnagrams(s, p)
        print(f's: "{s}", p: "{p}"')
        print(f"Anagram indices: {result}\n")
