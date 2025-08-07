"""
LeetCode 27: Remove Element
Difficulty: Easy
Pattern: Two Pointers - Same Direction

Given an integer array nums and an integer val, remove all occurrences of val 
in nums in-place. The relative order of the elements may be changed.

Example:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Constraints:
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100
"""

def removeElement(arr, val):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using two pointers technique
    Hint: Use slow pointer to track valid elements, fast pointer to iterate
    """
    l=0
    for r in range(1, len(arr)):
        if arr[r]!=val:
            l=l+1
            arr[r]=arr[l]
    return l+1

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 2, 2, 3], 3),
        ([0, 1, 2, 2, 3, 0, 4, 2], 2),
        ([1], 1),
        ([], 0)
    ]
    
    for nums, val in test_cases:
        original = nums.copy()
        length = removeElement(nums, val)
        print(f"Original: {original}, val: {val}")
        print(f"After removal: {nums[:length] if length else []}")
        print(f"Length: {length}\n")
