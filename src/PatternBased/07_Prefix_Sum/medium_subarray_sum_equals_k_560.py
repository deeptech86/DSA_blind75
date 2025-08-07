"""
LeetCode 560: Subarray Sum Equals K
Difficulty: Medium
Pattern: Prefix Sum

Given an array of integers nums and an integer k, return the total number of 
continuous subarrays whose sum equals to k.

Example:
Input: nums = [1, 1, 1], k = 2
Output: 2 (There are two subarrays: [1,1] and [1,1])

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7
"""

def subarraySum(nums, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    TODO: Implement the solution using prefix sum with HashMap
    Hint: Use cumulative sum and check if (current_sum - k) exists in hashmap
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1], 2),
        ([1, 2, 3], 3),
        ([1, -1, 0], 0),
        ([1, 2, 1, 2, 1], 3)
    ]
    
    for nums, k in test_cases:
        result = subarraySum(nums, k)
        print(f"nums: {nums}, k: {k}")
        print(f"Subarray count: {result}\n")
