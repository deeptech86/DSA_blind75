"""
LeetCode 4: Median of Two Sorted Arrays
Difficulty: Hard
Pattern: Binary Search

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the 
median of the two sorted arrays.

Example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.0
"""

def findMedianSortedArrays(nums1, nums2):
    """
    Time Complexity: O(log(min(m, n)))
    Space Complexity: O(1)
    """
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1
        
        # Handle edge cases
        max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        min_right1 = float('inf') if partition1 == m else nums1[partition1]
        
        max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        min_right2 = float('inf') if partition2 == n else nums2[partition2]
        
        # Check if we found the correct partition
        if max_left1 <= min_right2 and max_left2 <= min_right1:
            # We found the correct partition
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
            else:
                return max(max_left1, max_left2)
        elif max_left1 > min_right2:
            right = partition1 - 1
        else:
            left = partition1 + 1
    
    return -1

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
