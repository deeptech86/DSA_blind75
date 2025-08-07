"""
LeetCode 643: Maximum Average Subarray I
Difficulty: Easy
Pattern: Sliding Window (Fixed Window)

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value.

Example:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75 (Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75)

Constraints:
- n == nums.length
- 1 <= k <= n <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

def findMaxAverage(nums, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using sliding window technique
    Hint: Calculate sum of first k elements, then slide window and update sum
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 12, -5, -6, 50, 3], 4),
        ([5], 1),
        ([0, 1, 1, 3, 3], 4),
        ([-1], 1)
    ]
    
    for nums, k in test_cases:
        result = findMaxAverage(nums, k)
        print(f"nums: {nums}, k: {k}")
        print(f"Max average: {result}\n")
