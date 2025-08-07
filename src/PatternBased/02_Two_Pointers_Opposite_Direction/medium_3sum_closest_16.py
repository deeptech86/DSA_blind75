"""
LeetCode 16: 3Sum Closest
Difficulty: Medium
Pattern: Two Pointers - Opposite Direction

Given an integer array nums of length n and an integer target, find three integers 
in nums such that the sum is closest to target.

Example:
Input: nums = [-1,2,1,-4], target = 1
Output: 2 (The sum that is closest to the target is 2. (-1 + 2 + 1 = 2))

Constraints:
- 3 <= nums.length <= 1000
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4
"""

def threeSumClosest(nums, target):
    """
    Time Complexity: O(n²)
    Space Complexity: O(1)
    
    TODO: Implement the solution using sorting + two pointers technique
    Hint: Sort array, fix first element, use two pointers to find closest sum
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([-1, 2, 1, -4], 1),
        ([0, 0, 0], 1),
        ([1, 1, 1, 0], -100),
        ([4, 0, 5, -5, 3, 3, 0, -4, -5], -2)
    ]
    
    for nums, target in test_cases:
        result = threeSumClosest(nums, target)
        print(f"Input: {nums}, Target: {target}")
        print(f"Closest sum: {result}\n")
