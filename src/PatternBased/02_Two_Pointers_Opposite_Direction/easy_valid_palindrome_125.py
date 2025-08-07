"""
LeetCode 125: Valid Palindrome
Difficulty: Easy
Pattern: Two Pointers - Opposite Direction

A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters.
"""

def isPalindrome(s):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using two pointers technique
    Hint: Use left and right pointers, skip non-alphanumeric characters, compare case-insensitively
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "Madam",
        "No 'x' in Nixon"
    ]
    
    for s in test_cases:
        result = isPalindrome(s)
        print(f'String: "{s}"')
        print(f"Is palindrome: {result}\n")
