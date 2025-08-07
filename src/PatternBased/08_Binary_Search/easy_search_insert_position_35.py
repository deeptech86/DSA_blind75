"""
LeetCode 35: Search Insert Position
Difficulty: Easy
Pattern: Binary Search

Given a sorted array of distinct integers and a target value, return the index if 
the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example:
Input: nums = [1,3,5,6], target = 5
Output: 2

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums contains distinct values sorted in ascending order.
- -10^4 <= target <= 10^4
"""

def searchInsert(nums, target):
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    TODO: Implement the binary search algorithm to find insert position
    Hint: Use standard binary search, if not found, left pointer will be at insert position
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 3, 5, 6], 5),
        ([1, 3, 5, 6], 2),
        ([1, 3, 5, 6], 7),
        ([1, 3, 5, 6], 0)
    ]
    
    for nums, target in test_cases:
        result = searchInsert(nums, target)
        print(f"nums: {nums}, target: {target}")
        print(f"Insert position: {result}\n")
