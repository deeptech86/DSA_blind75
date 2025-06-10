"""
Problem: Product of Array Except Self
Technique: Prefix Sum
"""

def product_of_array_except_self(nums):
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to
    the product of all the elements of nums except nums[i].
    
    Args:
        nums: List[int] - Array of integers
        
    Returns:
        List[int] - Product of all elements except self
    """
    # TODO: Implement solution
    n = len(nums)
    pref = [1] * n

    total=1

    for i in range(len(nums)):
        if nums[i]!=0:
            total *= nums[i]
        else:
            total = 0

    for i in range(len(nums)):
            if nums[i] != 0:
                pref[i] = total//nums[i]
            else:
                pref[i] = total



    return pref




# Example 1
# Input: nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]
# Explanation: [1*2*3*4/1, 1*2*3*4/2, 1*2*3*4/3, 1*2*3*4/4]

# Example 2
# Input: nums = [-1, 1, 0, 3, -3]
# Output: [0, 0, 9, 0, 0]
# Explanation: Zero in the array causes most products to be zero

nums = [-1, 1, 0, 3, -3]
print(product_of_array_except_self(nums))
