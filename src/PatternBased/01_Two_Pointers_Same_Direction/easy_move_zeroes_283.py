"""
LeetCode 283: Move Zeroes
Difficulty: Easy
Pattern: Two Pointers - Same Direction

Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Example:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you minimize the total number of operations done?
"""

def moveZeroes(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using two pointers technique
    Hint: Use slow and fast pointers to track positions for non-zero elements
    """
    l,r=0,0
    for r in range(len(nums)):
        if nums[r]!=0:
            nums[l],nums[r] = nums[r],nums[l]
            l=l+1



# Test cases
if __name__ == "__main__":
    test_cases = [
        [0, 1, 0, 3, 12],
        [0],
        [1, 2, 3],
        [0, 0, 1]
    ]
    
    for nums in test_cases:
        original = nums.copy()
        moveZeroes(nums)
        print(f"Original: {original}")
        print(f"After moving zeros: {nums}\n")
