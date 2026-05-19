# #binary_search
# LeetCode 33: Search in Rotated Sorted Array
# Source: Code & Debug - DSA Python Course Part 52

from typing import List

def search(nums: List[int], target: int) -> int:
    """
    Search target in a rotated sorted array (no duplicates).

    Args:
        nums: A rotated sorted array of distinct integers
        target: The target value

    Returns:
        Index of target, or -1 if not found

    Example:
        search([4, 5, 6, 7, 0, 1, 2], 0) -> 4
    """
    # TODO: Implement your solution here
    pass


def test_search():
    # Test cases
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([1], 1) == 0
    assert search([3, 1], 1) == 1
    print("All test cases passed!")


if __name__ == "__main__":
    test_search()
