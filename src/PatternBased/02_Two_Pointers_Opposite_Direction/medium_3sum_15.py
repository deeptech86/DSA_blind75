"""
LeetCode 15: 3Sum
Difficulty: Medium
Pattern: Two Pointers - Opposite Direction

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Example:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Constraints:
- 3 <= nums.length <= 3000
- -10^5 <= nums[i] <= 10^5

Note: The solution set must not contain duplicate triplets.
"""

def threeSum(nums):
    """
    Time Complexity: O(n²)
    Space Complexity: O(1) - excluding output space
    
    TODO: Implement the solution using sorting + two pointers technique
    Hint: Sort array, fix first element, use two pointers for remaining two elements
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [0, 1, 1],
        [0, 0, 0],
        [-2, 0, 0, 2, 2]
    ]
    
    for nums in test_cases:
        result = threeSum(nums)
        print(f"Input: {nums}")
        print(f"Triplets: {result}\n")
