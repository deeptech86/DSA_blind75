"""
LeetCode 33: Search in Rotated Sorted Array
Difficulty: Medium
Pattern: Binary Search

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at some pivot index.
Given the array nums after the possible rotation and an integer target, return the 
index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Constraints:
- 1 <= nums.length <= 5000
- -10^4 <= nums[i] <= 10^4
- All values of nums are unique.
- nums is an ascending array that is possibly rotated.
- -10^4 <= target <= 10^4
"""

def search(nums, target):
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using binary search on rotated array
    Hint: Determine which half is sorted, then check if target lies in that sorted half
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([4, 5, 6, 7, 0, 1, 2], 3),
        ([1], 0),
        ([1, 3], 3)
    ]
    
    for nums, target in test_cases:
        result = search(nums, target)
        print(f"nums: {nums}, target: {target}")
        print(f"Index: {result}\n")
