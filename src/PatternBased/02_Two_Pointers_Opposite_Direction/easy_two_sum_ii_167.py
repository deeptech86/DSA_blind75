"""
LeetCode 167: Two Sum II - Input Array Is Sorted
Difficulty: Easy
Pattern: Two Pointers - Opposite Direction

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing 
order, find two numbers such that they add up to a specific target number.

Example:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

Constraints:
- 2 <= numbers.length <= 3 * 10^4
- -1000 <= numbers[i] <= 1000
- numbers is sorted in non-decreasing order.
- -1000 <= target <= 1000
- The tests are generated such that there is exactly one solution.
"""

def twoSum(numbers, target):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using two pointers technique
    Hint: Use left and right pointers, adjust based on sum comparison with target
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([2, 3, 4], 6),
        ([-1, 0], -1),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8)
    ]
    
    for numbers, target in test_cases:
        result = twoSum(numbers, target)
        print(f"Numbers: {numbers}, Target: {target}")
        print(f"Indices: {result}\n")
