"""
LeetCode 153: Find Minimum in Rotated Sorted Array
Difficulty: Medium
Pattern: Binary Search

Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example:
Input: nums = [3,4,5,1,2]
Output: 1

Constraints:
- n == nums.length
- 1 <= n <= 5000
- -5000 <= nums[i] <= 5000
- All the integers of nums are unique.
- nums is sorted and rotated between 1 and n times.
"""

def findMin(nums):
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using binary search
    Hint: Compare mid element with rightmost element to decide which half to search
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [3, 4, 5, 1, 2],
        [4, 5, 6, 7, 0, 1, 2],
        [11, 13, 15, 17],
        [1, 2]
    ]
    
    for nums in test_cases:
        result = findMin(nums)
        print(f"nums: {nums}")
        print(f"Minimum: {result}\n")
