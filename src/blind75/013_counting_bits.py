"""
Problem: Counting Bits
Technique: Bit Manipulation, Dynamic Programming
"""

def counting_bits(n):
    """
    Given an integer n, return an array ans of length n + 1 such that
    for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
    
    Args:
        n: int - An integer
        
    Returns:
        List[int] - Array where each element is the count of 1's in binary representation
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: n = 2
# Output: [0, 1, 1]
# Explanation: 0 → 0 has 0 '1's, 1 → 1 has 1 '1', 2 → 10 has 1 '1'

# Example 2
# Input: n = 5
# Output: [0, 1, 1, 2, 1, 2]
# Explanation: 0 → 0 has 0 '1's, 1 → 1 has 1 '1', 2 → 10 has 1 '1', 3 → 11 has 2 '1's, 4 → 100 has 1 '1', 5 → 101 has 2 '1's
