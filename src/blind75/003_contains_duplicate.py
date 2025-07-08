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
    hashset=set()
    current=1
    for current in range(len(nums)):
        if nums[current] in hashset:
            return True
        else:
            hashset.add(nums[current])
    return False


# Example 1
# Input: nums = [1, 2, 3, 1]
# Output: True
# Explanation: There is a duplicate of 1 in the array

# Example 2
# Input: nums = [1, 2, 3, 4]
# Output: False
# Explanation: No duplicates in the array


nums = [1, 2, 3, 4]
print(contains_duplicate(nums))
# def remove_duplicate(nums):
#     slow, fast =0,1
#     while fast < len(nums):
#         if nums[slow]==nums[fast]:
#             slow+=1
#         else:
#             fast+=1
#     return nums
#
# print(remove_duplicate(nums))