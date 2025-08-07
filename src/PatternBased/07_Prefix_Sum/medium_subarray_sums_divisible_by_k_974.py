"""
LeetCode 974: Subarray Sums Divisible by K
Difficulty: Medium
Pattern: Prefix Sum

Given an integer array nums and an integer k, return the number of non-empty 
subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7 (There are 7 subarrays with a sum divisible by 5)

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- 2 <= k <= 10^4
"""

def subarraysDivByK(nums, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(k)
    
    TODO: Implement the solution using prefix sum with modular arithmetic
    Hint: Count remainders of prefix sums, if two prefix sums have same remainder, their difference is divisible by k
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([4, 5, 0, -2, -3, 1], 5),
        ([5], 9),
        ([1, 2, 3], 3),
        ([-1, 2, 9], 2)
    ]
    
    for nums, k in test_cases:
        result = subarraysDivByK(nums, k)
        print(f"nums: {nums}, k: {k}")
        print(f"Subarray count divisible by k: {result}\n")
