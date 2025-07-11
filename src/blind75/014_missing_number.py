"""
Problem: Missing Number
Technique: Bit Manipulation, Math
"""

def missing_number(nums):
    """
    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.
    
    Args:
        nums: List[int] - Array of distinct integers
        
    Returns:
        int - The missing number in the range
    """
    # TODO: Implement solution
    # max= nums[0]
    # min =nums[0]
    # # for i in range(1,len(nums)):
    # #     if nums[i] > max :
    # #         max= nums[i]
    # #     elif nums[i] < min:
    # #         min = nums[i]
    new_arr = sorted(nums)
    for i in range(len(new_arr)-1):
        if new_arr[i] + 1 != new_arr[i+1] :
            return new_arr[i] + 1



# Example 1
# Input: nums = [3, 0, 1]
# Output: 2
# Explanation: The array should contain all numbers from 0 to 3, but 2 is missing

# Example 2
# Input: nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
# Output: 8
# Explanation: The array should contain all numbers from 0 to 9, but 8 is missing
nums = [9, 6, 4,  3, 5, 7, 8 ,11]
print(missing_number(nums))