"""
LeetCode 327: Count of Range Sum
Difficulty: Hard
Pattern: Prefix Sum

Given an integer array nums and two integers lower and upper, return the number of 
range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.

Example:
Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3 (The three ranges are: [0,0], [2,2], and [0,2])

Constraints:
- 1 <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1
- -10^5 <= lower <= upper <= 10^5

Note: The answer is guaranteed to fit in a 32-bit integer.
"""

def countRangeSum(nums, lower, upper):
    """
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    TODO: Implement the solution using merge sort with prefix sums
    Hint: Use divide and conquer, count valid range sums while merging sorted halves
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([-2, 5, -1], -2, 2),
        ([0], 0, 0),
        ([-2147483647, 0, -2147483647, 2147483647], -564, 3864)
    ]
    
    for nums, lower, upper in test_cases:
        result = countRangeSum(nums, lower, upper)
        print(f"nums: {nums}, lower: {lower}, upper: {upper}")
        print(f"Range sum count: {result}\n")
