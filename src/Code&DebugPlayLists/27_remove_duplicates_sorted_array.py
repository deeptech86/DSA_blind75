# #array #two_pointers
# LeetCode 26: Remove Duplicates from a Sorted Array
# Source: Code & Debug - DSA Python Course Part 27

from typing import List

def remove_duplicates(nums: List[int]) -> int:
    """
    Remove duplicates from a sorted array in-place.
    Return the number of unique elements.

    Args:
        nums: A sorted list of integers (modified in-place)

    Returns:
        The number of unique elements

    Example:
        nums = [1, 1, 2]
        k = remove_duplicates(nums)  # k = 2, nums[:k] = [1, 2]
    """
    # TODO: Implement your solution here
    i=0
    j=1
    counter=0
    n=len(nums)
    if n==0 or n==1:
        return n
    else:
        while j<n:
            if nums[i]!=nums[j]:
                i += 1
                nums[i],nums[j]= nums[j],nums[i]

                counter+=1
            j+=1
        print(nums[:counter+1])
        return counter+1








def test_remove_duplicates():
    # Test cases
    nums2 = [0, 0, 0, 1, 1, 2, 2, 3, 3, 4]
    assert remove_duplicates(nums2) == 5
    assert nums2[:5] == [0, 1, 2, 3, 4]

    nums1 = [1, 1, 2]
    assert remove_duplicates(nums1) == 2
    assert nums1[:2] == [1, 2]



    nums3 = [1]
    assert remove_duplicates(nums3) == 1

    nums4 = []
    assert remove_duplicates(nums4) == 0

    print("All test cases passed!")


if __name__ == "__main__":
    test_remove_duplicates()
