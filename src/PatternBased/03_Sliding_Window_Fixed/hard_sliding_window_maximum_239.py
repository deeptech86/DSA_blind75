"""
LeetCode 239: Sliding Window Maximum
Difficulty: Hard
Pattern: Sliding Window (Fixed Window)

You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window 
moves right by one position. Return the max sliding window.

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
"""

def maxSlidingWindow(nums, k):
    """
    Time Complexity: O(n)
    Space Complexity: O(k)
    
    TODO: Implement the solution using deque (double-ended queue)
    Hint: Use deque to store indices in decreasing order of their values
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3),
        ([1], 1),
        ([1, -1], 1),
        ([9, 11], 2),
        ([4, -2], 2)
    ]
    
    for nums, k in test_cases:
        result = maxSlidingWindow(nums, k)
        print(f"nums: {nums}, k: {k}")
        print(f"Sliding window maximum: {result}\n")
