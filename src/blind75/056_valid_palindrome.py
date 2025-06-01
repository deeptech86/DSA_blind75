"""
Problem: Valid Palindrome
Technique: Two Pointers (Opposite Direction)
"""

def valid_palindrome(s):
    """
    Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
    
    Args:
        s: str - Input string
        
    Returns:
        bool - True if the string is a palindrome, False otherwise
    """
    # TODO: Implement solution

    # char = (''.join  for c in s.split(' '))
    char = list(word.lower() for word in s if word not in [' ',",",":"])
    left, right = 0, len(char) - 1
    while left<right:
        if char[left]== char[right]:
            left+=1
            right-=1
        else:
            return False
    return True



# Example 1
# Input: s = "A man, a plan, a canal: Panama"
# Output: True
# Explanation: "amanaplanacanalpanama" is a palindrome when ignoring non-alphanumeric characters and case

# Example 2
# Input: s = "race a car"
# Output: False
# Explanation: "raceacar" is not a palindrome

s = "A man, a plan, a canal: Panama"
print(valid_palindrome(s))