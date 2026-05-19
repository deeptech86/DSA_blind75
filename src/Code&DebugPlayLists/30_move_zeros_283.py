# #array #two_pointers
# LeetCode 283: Move Zeros to the End of the List
# Source: Code & Debug - DSA Python Course Part 30

from typing import List

def move_zeroes(nums: List[int]) -> None:
    """
    Move all 0's to the end while maintaining relative order of non-zero elements.
    Must be done in-place without making a copy.

    Args:
        nums: A list of integers (modified in-place)

    Example:
        nums = [0, 1, 0, 3, 12]
        move_zeroes(nums)  # nums becomes [1, 3, 12, 0, 0]
    """
    # TODO: Implement your solution here



def test_move_zeroes():
    # Test cases
    nums1 = [0, 1, 0, 3, 12]
    move_zeroes(nums1)
    assert nums1 == [1, 3, 12, 0, 0]

    nums2 = [0]
    move_zeroes(nums2)
    assert nums2 == [0]

    nums3 = [1, 2, 3]
    move_zeroes(nums3)
    assert nums3 == [1, 2, 3]

    nums4 = [0, 0, 1]
    move_zeroes(nums4)
    assert nums4 == [1, 0, 0]

    print("All test cases passed!")


if __name__ == "__main__":
    test_move_zeroes()
