"""
LeetCode 209: Minimum Size Subarray Sum
Difficulty: Medium
Pattern: Sliding Window (Shortest Variable Window)

Given an array of positive integers nums and a positive integer target, return the 
minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of 
which the sum is greater than or equal to target. If there is no such subarray, return 0.

Example:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2 (The subarray [4,3] has the minimal length under the problem constraint)

Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another solution 
of which the time complexity is O(n log(n)).
"""

def minSubArrayLen(target, nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using sliding window technique
    Hint: Expand right pointer to increase sum, contract left pointer when sum >= target
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        (7, [2, 3, 1, 2, 4, 3]),
        (4, [1, 4, 4]),
        (11, [1, 1, 1, 1, 1, 1, 1, 1]),
        (15, [1, 2, 3, 4, 5])
    ]
    
    for target, nums in test_cases:
        result = minSubArrayLen(target, nums)
        print(f"target: {target}, nums: {nums}")
        print(f"Minimum subarray length: {result}\n")
