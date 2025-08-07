"""
LeetCode 862: Shortest Subarray with Sum at Least K
Difficulty: Hard
Pattern: Sliding Window (Shortest Variable Window)

Given an integer array nums and an integer k, return the length of the shortest 
non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.

Example:
Input: nums = [1], k = 1
Output: 1

Constraints:
- 1 <= nums.length <= 10^5
- -10^5 <= nums[i] <= 10^5
- 1 <= k <= 10^9
"""

def shortestSubarray(nums, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    
    TODO: Implement the solution using deque with prefix sums
    Hint: This problem has negative numbers, so sliding window won't work directly. Use deque with prefix sums.
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1], 1),
        ([1, 2], 4),
        ([2, -1, 2], 3),
        ([84, -37, 32, 40, 95], 167)
    ]
    
    for nums, k in test_cases:
        result = shortestSubarray(nums, k)
        print(f"nums: {nums}, k: {k}")
        print(f"Shortest subarray length: {result}\n")
