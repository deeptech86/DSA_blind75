"""
LeetCode 424: Longest Repeating Character Replacement
Difficulty: Medium
Pattern: Sliding Window (Longest Variable Window)

You are given a string s and an integer k. You can choose any character of the string 
and change it to any other uppercase English character. You can perform this operation 
at most k times. Return the length of the longest substring containing the same letter 
you can get after performing the above operations.

Example:
Input: s = "ABAB", k = 2
Output: 4 (Replace the two 'A's with two 'B's or vice versa)

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters.
- 0 <= k <= s.length
"""

def characterReplacement(s, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(1) - at most 26 characters
    
    TODO: Implement the solution using sliding window technique
    Hint: Track character frequencies, find most frequent char in window, check if window is valid
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("ABAB", 2),
        ("AABABBA", 1),
        ("ABCDE", 1),
        ("AAAA", 0)
    ]
    
    for s, k in test_cases:
        result = characterReplacement(s, k)
        print(f'String: "{s}", k: {k}')
        print(f"Longest repeating character replacement: {result}\n")
