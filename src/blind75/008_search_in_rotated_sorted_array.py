"""
Problem: Search in Rotated Sorted Array
Technique: Binary Search
"""


def search_in_rotated_sorted_array(nums, target):
    """
    Given a rotated sorted array nums and a target value, return the index of target if it's in nums,
    or -1 if it's not in nums.

    Args:
        nums: List[int] - Rotated sorted array
        target: int - Target value to search for

    Returns:
        int - Index of target in nums, or -1 if not found
    """
    # TODO: Implement solution
    left, right = 0, len(nums)
    mid = left + (right - left) // 2
    while left < right:
        if mid == target:
            return mid
        elif nums[mid] < nums[left]:
            left = mid + 1
        else:
            right = right - 1
    return -1


# Example 1
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
# Output: 4
# Explanation: 0 is found at index 4

# Example 2
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
# Output: -1
# Explanation: 3 is not in the array


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print (search_in_rotated_sorted_array(nums, target))
