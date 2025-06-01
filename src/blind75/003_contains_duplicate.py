"""
Problem: Contains Duplicate
Technique: Hash Table
"""

def contains_duplicate(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
    
    Args:
        nums: List[int] - Array of integers
        
    Returns:
        bool - True if array contains duplicates, False otherwise
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: nums = [1, 2, 3, 1]
# Output: True
# Explanation: There is a duplicate of 1 in the array

# Example 2
# Input: nums = [1, 2, 3, 4]
# Output: False
# Explanation: No duplicates in the array


nums = [0, 0, 1, 1, 1, 2, 2]
def remove_duplicate(nums):
    slow, fast =0,1
    while fast < len(nums):
        if nums[slow]==nums[fast]:
            nums.remove(nums[slow])
            slow+=1
        else:
            fast+=1
    return nums

print(remove_duplicate(nums))