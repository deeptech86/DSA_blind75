"""
Problem: Maximum Product Subarray
Technique: Dynamic Programming (Aggregation and Memoization)
"""

def maximum_product_subarray(nums):
    """
    Given an integer array nums, find the contiguous subarray within an array
    which has the largest product, and return the product.
    
    Args:
        nums: List[int] - Array of integers
        
    Returns:
        int - Product of contiguous subarray with largest product
    """
    # TODO: Implement solution
    best_prod = nums[0]
    current_prod= 1
    
    for i in nums:
        # current_prod = max(i, current_prod*i)
        current_prod *= i
        best_prod = max(current_prod,best_prod)
        
    return best_prod



# Example 1
# Input: nums = [2, 3, -2, 4]
# Output: 6
# Explanation: The subarray [2, 3] has the largest product = 6

# Example 2
# Input: nums = [-2, 0, -1]
# Output: 0
# Explanation: The result cannot be negative, so we return 0


nums = [2, 3, -2, 4]
print(maximum_product_subarray(nums))