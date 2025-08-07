"""
LeetCode 724: Find Pivot Index
Difficulty: Easy
Pattern: Prefix Sum

Given an array of integers nums, calculate the pivot index of this array.
The pivot index is the index where the sum of all the numbers strictly to the left 
of the index is equal to the sum of all the numbers strictly to the right of the index.

Example:
Input: nums = [1, 7, 3, 6, 5, 6]
Output: 3 (Left sum = 1 + 7 + 3 = 11, Right sum = 5 + 6 = 11)

Constraints:
- 1 <= nums.length <= 10^4
- -1000 <= nums[i] <= 1000

Note: If no such index exists, return -1. If there are multiple pivot indexes, 
return the left-most pivot index.
"""

def pivotIndex(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using prefix sum technique
    Hint: Calculate total sum first, then iterate comparing left sum with right sum
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [1, 7, 3, 6, 5, 6],
        [1, 2, 3],
        [2, 1, -1],
        [1]
    ]
    
    for nums in test_cases:
        result = pivotIndex(nums)
        print(f"nums: {nums}")
        print(f"Pivot index: {result}\n")
