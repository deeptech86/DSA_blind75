"""
LeetCode 80: Remove Duplicates from Sorted Array II
Difficulty: Medium
Pattern: Two Pointers - Same Direction

Given an integer array nums sorted in non-decreasing order, remove some duplicates 
in-place such that each unique element appears at most twice. The relative order 
of the elements should be kept the same.

Example:
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order.
"""

def removeDuplicates(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using two pointers technique
    Hint: Start slow pointer from index 2, compare with element two positions back
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [1, 1, 1, 2, 2, 3],
        [0, 0, 1, 1, 1, 1, 2, 3, 3],
        [1, 1],
        [1]
    ]
    
    for nums in test_cases:
        original = nums.copy()
        length = removeDuplicates(nums)
        print(f"Original: {original}")
        print(f"After removal: {nums[:length] if length else []}")
        print(f"Length: {length}\n")
