"""
LeetCode 42: Trapping Rain Water
Difficulty: Hard
Pattern: Two Pointers - Same Direction

Given n non-negative integers representing an elevation map where the width of 
each bar is 1, compute how much water it can trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water are being trapped.

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 3 * 10^4
"""

def trap(height):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using two pointers technique
    Hint: Use left and right pointers with left_max and right_max to track water levels
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        [4, 2, 0, 3, 2, 5],
        [3, 0, 2, 0, 4],
        [1, 1, 1]
    ]
    
    for height in test_cases:
        result = trap(height)
        print(f"Height: {height}")
        print(f"Water trapped: {result}\n")
