"""
LeetCode 340: Longest Substring with At Most K Distinct Characters
Difficulty: Medium
Pattern: Sliding Window (Longest Variable Window)

Given a string s and an integer k, return the length of the longest substring 
of s that contains at most k distinct characters.

Example:
Input: s = "eceba", k = 2
Output: 3 (The longest substring is "ece" with length 3)

Constraints:
- 1 <= s.length <= 10^4
- 0 <= k <= 50
"""

def lengthOfLongestSubstringKDistinct(s, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(k)
    
    TODO: Implement the solution using sliding window technique
    Hint: Use dictionary to count characters, expand right, shrink left when distinct chars > k
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ("eceba", 2),
        ("aa", 1), 
        ("abaccc", 2),
        ("", 2)
    ]
    
    for s, k in test_cases:
        result = lengthOfLongestSubstringKDistinct(s, k)
        print(f's: "{s}", k: {k}')
        print(f"Longest substring length: {result}\n")
