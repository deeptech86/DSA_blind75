# #array
# LeetCode 189: Rotate Array by K Places
# Source: Code & Debug - DSA Python Course Part 29

from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Rotate array to the right by k steps in-place.

    Args:
        nums: A list of integers (modified in-place)
        k: Number of steps to rotate

    Example:
        nums = [1, 2, 3, 4, 5, 6, 7], k = 3
        rotate(nums, k)  # nums becomes [5, 6, 7, 1, 2, 3, 4]
    """
    # TODO: Implement your solution here


    def reversehelper(nums,start,end):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start=start+1
            end=end-1

    n = len(nums)
    if n<=1:
        return n
    else:
        reversehelper(nums, n-k, n - 1)
        print(nums)
        reversehelper(nums, 0, n-k - 1)
        print(nums)
        reversehelper(nums, 0, n - 1)

        print(nums)


def test_rotate():
    # Test cases
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums1, 3)
    assert nums1 == [5, 6, 7, 1, 2, 3, 4]

    nums2 = [-1, -100, 3, 99]
    rotate(nums2, 2)
    assert nums2 == [3, 99, -1, -100]

    nums3 = [1, 2]
    rotate(nums3, 3)
    assert nums3 == [2, 1]

    nums4 = [1]
    rotate(nums4, 0)
    assert nums4 == [1]

    print("All test cases passed!")


if __name__ == "__main__":
    test_rotate()
