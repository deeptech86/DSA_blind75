"""
LeetCode 26: Remove Duplicates from Sorted Array
Difficulty: Easy
Pattern: Two Pointers - Same Direction

Given an integer array nums sorted in non-decreasing order, remove the duplicates 
in-place such that each unique element appears only once. The relative order of 
the elements should be kept the same.

Example:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.
"""

def removeDuplicates(nums):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using two pointers technique
    Hint: Use slow and fast pointers, increment slow only when elements differ
    """
    l = 0
    for r in range(1,len(nums)):
        if nums[r]!=nums[l]:
            # nums.remove(nums[r])
            l=l+1
            nums[l]=nums[r]
    return l+1
    # return len(nums) - len(set(nums))
    # for i in range(len(nums)):
    # res_arr=[]
    # snowball=0
    # for i in nums:
    #     if i not in res_arr:
    #         res_arr.append(i)
    #
    #     else:
    #         snowball+=1
    # return snowball







# Test cases
if __name__ == "__main__":
    test_cases = [
        [2,2,3,5,6,3,4,5],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
        [1],
        []
    ]
    
    for nums in test_cases:
        original = nums.copy()
        length = removeDuplicates(nums)
        print(f"Original: {original}")
        print(f"After removal: {nums[:length] if length else []}")
        print(f"Length: {length}\n")
