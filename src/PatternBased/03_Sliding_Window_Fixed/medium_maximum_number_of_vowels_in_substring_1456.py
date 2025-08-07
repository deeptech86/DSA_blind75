"""
LeetCode 1456: Maximum Number of Vowels in a Substring of Given Length
Difficulty: Medium
Pattern: Sliding Window (Fixed Window)

Given a string s and an integer k, return the maximum number of vowel letters 
in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example:
Input: s = "abciiidef", k = 3
Output: 3 (The substring "iii" contains 3 vowel letters)

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- 1 <= k <= s.length
"""

def maxVowels(s, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using sliding window technique
    Hint: Count vowels in first window, then slide and update count
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("abciiidef", 3),
        ("aeiou", 2),
        ("leetcode", 3),
        ("rhythms", 4),
        ("tryhard", 4)
    ]
    
    for s, k in test_cases:
        result = maxVowels(s, k)
        print(f'String: "{s}", k: {k}')
        print(f"Max vowels: {result}\n")
