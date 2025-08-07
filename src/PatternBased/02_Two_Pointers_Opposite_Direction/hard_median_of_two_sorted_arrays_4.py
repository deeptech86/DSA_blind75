"""
LeetCode 4: Median of Two Sorted Arrays
Difficulty: Hard
Pattern: Two Pointers - Opposite Direction / Binary Search

Given two sorted arrays nums1 and nums2 of size m and n respectively, 
return the median of the two sorted arrays.

Example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0

Constraints:
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6

Follow up: The overall run time complexity should be O(log (m+n)).
"""

def findMedianSortedArrays(nums1, nums2):
    """
    Time Complexity: O(log(min(m, n)))
    Space Complexity: O(1)
    
    TODO: Implement the solution using binary search technique
    Hint: Use binary search on the smaller array to find the correct partition
    """
    pass

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 3], [2]),
        ([1, 2], [3, 4]),
        ([0, 0], [0, 0]),
        ([], [1]),
        ([2], [])
    ]
    
    for nums1, nums2 in test_cases:
        result = findMedianSortedArrays(nums1, nums2)
        print(f"nums1: {nums1}, nums2: {nums2}")
        print(f"Median: {result}\n")
