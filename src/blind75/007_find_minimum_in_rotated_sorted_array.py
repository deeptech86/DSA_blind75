"""
Problem: Find Minimum in Rotated Sorted Array
Technique: Binary Search
"""

def find_minimum_in_rotated_sorted_array(nums):
    """
    Given a sorted array nums that is rotated at an unknown pivot, find the minimum element.
    
    Args:
        nums: List[int] - Rotated sorted array
        
    Returns:
        int - Minimum element in the array
    """
    # TODO: Implement solution
    min_value= min(nums)
    get_index= nums.index(min_value)
    print(get_index)


# Example 1
# Input: nums = [3, 4, 5, 1, 2]
# Output: 1
# Explanation: The original array was [1, 2, 3, 4, 5] rotated 3 times

# Example 2
# Input: nums = [4, 5, 6, 7, 8, 9, 0, 1, 2]
# Output: 0
# Explanation: The original array was [0, 1, 2, 4, 5, 6, 7] rotated 4 times

nums = [3, 4, 5, 1, 2]
find_minimum_in_rotated_sorted_array(nums)