# #binary_search
# LeetCode 153: Find Minimum in Rotated Sorted Array
# Source: Code & Debug - DSA Python Course Part 54

from typing import List

def find_min(nums: List[int]) -> int:
    """
    Find the minimum element in a rotated sorted array.

    Args:
        nums: A rotated sorted array of unique elements

    Returns:
        The minimum element

    Example:
        find_min([3, 4, 5, 1, 2]) -> 1
    """
    # TODO: Implement your solution here
    pass


def test_find_min():
    # Test cases
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([11, 13, 15, 17]) == 11
    assert find_min([2, 1]) == 1
    assert find_min([1]) == 1
    print("All test cases passed!")


if __name__ == "__main__":
    test_find_min()
