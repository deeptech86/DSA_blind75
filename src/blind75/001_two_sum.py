"""
Problem: Two Sum
Technique: Hash Table
"""

def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    
    Args:
        nums: List[int] - Array of integers
        target: int - Target sum
        
    Returns:
        List[int] - Indices of the two numbers
    """
    # TODO: Implement solution
    # slow, fast =0,len(nums)-1
    # sum = nums[slow]+nums[fast]
    # while slow<fast:
    #     if sum>target:
    #
    #         slow += 1
    #     if sum<target:
    #         fast -= 1
    #     else:
    #         return [slow,fast]
    # return -1 #Target not found
    start=0
    while start<len(nums):
        if (target - nums[start]) in nums:
            if nums.index(target-nums[start]) != start:
                return [start, nums.index(target-nums[start])]
            start+=1
    return -1



# Example 1
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9

# Example 2
# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Explanation: nums[1] + nums[2] = 2 + 4 = 6

nums = [3, 3, 4]
target = 6
print(two_sum(nums, target))