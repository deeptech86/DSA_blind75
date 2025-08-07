"""
LeetCode 287: Find the Duplicate Number
Difficulty: Medium
Pattern: Fast and Slow Pointers

Given an array of integers nums containing n + 1 integers where each integer is 
in the range [1, n] inclusive. There is only one repeated number in nums, return 
this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example:
Input: nums = [1,3,4,2,2]
Output: 2

Constraints:
- 1 <= n <= 10^5
- nums.length == n + 1
- 1 <= nums[i] <= n
- All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:
- How can we prove that at least one duplicate number must exist in nums?
- Can you solve the problem in linear runtime complexity?
"""

def findDuplicate(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using Floyd's cycle detection algorithm
    Hint: Treat array as linked list where nums[i] points to nums[nums[i]], find cycle entrance
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2],
        [1, 1],
        [1, 1, 2]
    ]
    
    for nums in test_cases:
        result = findDuplicate(nums)
        print(f"nums: {nums}")
        print(f"Duplicate: {result}\n")
