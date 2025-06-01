"""
Problem: House Robber II
Technique: Dynamic Programming (Aggregation and Memoization)
"""

def house_robber_ii(nums):
    """
    Given an integer array nums representing the amount of money of each house,
    return the maximum amount of money you can rob without alerting the police.
    All houses are arranged in a circle (first and last houses are adjacent).
    
    Args:
        nums: List[int] - Array of money in each house
        
    Returns:
        int - Maximum amount of money that can be robbed
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: nums = [2, 3, 2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent in a circle

# Example 2
# Input: nums = [1, 2, 3, 1]
# Output: 4
# Explanation: Rob house 2 (money = 2) and then rob house 4 (money = 1). Rob house 1 (money = 1) and then rob house 3 (money = 3).
