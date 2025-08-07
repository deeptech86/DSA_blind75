"""
LeetCode 704: Binary Search
Difficulty: Easy
Pattern: Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.

Example:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 < nums[i], target < 10^4
- All the integers in nums are unique.
- nums is sorted in ascending order.

You must write an algorithm with O(log n) runtime complexity.
"""

def search(nums, target):
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)
    
    TODO: Implement the binary search algorithm
    Hint: Use left and right pointers, compare middle element with target
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([-1, 0, 3, 5, 9, 12], 9),
        ([-1, 0, 3, 5, 9, 12], 2),
        ([5], 5),
        ([1, 2, 3, 4, 5], 3)
    ]
    
    for nums, target in test_cases:
        result = search(nums, target)
        print(f"nums: {nums}, target: {target}")
        print(f"Index: {result}\n")
