"""
LeetCode 3: Longest Substring Without Repeating Characters
Difficulty: Medium
Pattern: Sliding Window (Longest Variable Window)

Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3 (The answer is "abc", with the length of 3)

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s):
    """
    Time Complexity: O(n)
    Space Complexity: O(min(m,n)) where m is charset size
    
    TODO: Implement the solution using sliding window technique
    Hint: Use a set to track characters in current window, expand and contract window as needed
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        "abcabcbb",
        "bbbbb", 
        "pwwkew",
        "",
        "dvdf"
    ]
    
    for s in test_cases:
        result = lengthOfLongestSubstring(s)
        print(f'String: "{s}"')
        print(f"Longest substring length: {result}\n")
