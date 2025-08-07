"""
LeetCode 303: Range Sum Query - Immutable
Difficulty: Easy
Pattern: Prefix Sum

Given an integer array nums, handle multiple queries of the following type:
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:
- NumArray(int[] nums) Initializes the object with the integer array nums.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive.

Example:
Input: nums = [-2, 0, 3, -5, 2, -1]
Output: sumRange(0, 2) = 1, sumRange(2, 5) = -1, sumRange(0, 5) = -3

Constraints:
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
- 0 <= left <= right < nums.length
- At most 10^4 calls will be made to sumRange.
"""

class NumArray:
    def __init__(self, nums):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        TODO: Initialize the prefix sum array
        Hint: Create an array where prefix_sum[i] = sum of elements from 0 to i-1
        """
        pass
    
    def sumRange(self, left, right):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        
        TODO: Calculate range sum using prefix sum array
        Hint: sum(left, right) = prefix_sum[right+1] - prefix_sum[left]
        """
        pass

# Test cases
if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    num_array = NumArray(nums)
    
    queries = [(0, 2), (2, 5), (0, 5)]
    
    print(f"nums: {nums}")
    for left, right in queries:
        result = num_array.sumRange(left, right)
        print(f"sumRange({left}, {right}) = {result}")
