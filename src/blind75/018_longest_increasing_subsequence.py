"""
Problem: Longest Increasing Subsequence
Technique: Dynamic Programming (Aggregation and Memoization)
"""

def longest_increasing_subsequence(nums):
    """
    Given an integer array nums, return the length of the longest strictly increasing subsequence.
    
    Args:
        nums: List[int] - Array of integers
        
    Returns:
        int - Length of the longest increasing subsequence
    """
    # TODO: Implement solution
    substring =[]
    substring.append(nums[0])
    lastadded =0

    for i in range(1,len(nums)):
        if substring[0] >= nums[i]:
            substring[0]=nums[i]
        else:

            if  substring[-1] > nums[i]:
                substring.pop()

            substring.append(nums[i])
    print(str(substring))
    return len(substring)




# Example 1
# Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4
# Explanation: The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4

# Example 2
# Input: nums = [0, 1, 0, 3, 2, 3]
# Output: 4
# Explanation: The longest increasing subsequence is [0, 1, 2, 3], therefore the length is 4


nums = [0, 1, 0, 3, 2, 3]
print(longest_increasing_subsequence(nums))