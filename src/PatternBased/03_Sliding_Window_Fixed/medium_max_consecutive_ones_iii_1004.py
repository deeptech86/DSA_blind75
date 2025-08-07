"""
LeetCode 1004: Max Consecutive Ones III
Difficulty: Medium
Pattern: Sliding Window (Variable Window)

Given a binary array nums and an integer k, return the maximum number of 
consecutive 1's in the array if you can flip at most k 0's.

Example:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6 (Flip the two 0's to get [1,1,1,1,1,1,1,1,1,1,0])

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
- 0 <= k <= nums.length
"""

def longestOnes(nums, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using sliding window technique
    Hint: Use two pointers, expand right, shrink left when zeros > k
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2),
        ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3),
        ([1, 1, 1, 1], 0),
        ([0, 0, 0, 0], 2)
    ]
    
    for nums, k in test_cases:
        result = longestOnes(nums, k)
        print(f"nums: {nums}, k: {k}")
        print(f"Max consecutive ones: {result}\n")
