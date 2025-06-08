"""
Problem: Maximum Subarray
Technique: Dynamic Programming (Aggregation and Memoization)
"""

def maximum_subarray(nums):
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum.
    
    Args:
        nums: List[int] - Array of integers
        
    Returns:
        int - Sum of contiguous subarray with largest sum
    """
    # TODO: Implement solution
    best_sum = nums[0]
    current_sum =0
    for i in nums:
        current_sum= max(i,current_sum+i)
        best_sum = max(best_sum,current_sum)
    return best_sum


# Example 1
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: The subarray [4, -1, 2, 1] has the largest sum = 6

# Example 2
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum = 1

# Kadane Algo template
# best_sum=arr[0]
# current_sum = 0
# for i in nums:
#     current_sum =max(i,current_sum+i)
#     best_sum = max(best_sum,current_sum)
# return best_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maximum_subarray(nums))