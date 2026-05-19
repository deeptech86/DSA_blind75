# #binary_search
# LeetCode 81: Search in Rotated Sorted Array II (with duplicates)
# Source: Code & Debug - DSA Python Course Part 53

from typing import List

def search(nums: List[int], target: int) -> bool:
    """
    Search target in a rotated sorted array (may have duplicates).

    Args:
        nums: A rotated sorted array (may contain duplicates)
        target: The target value

    Returns:
        True if target exists, False otherwise

    Example:
        search([2, 5, 6, 0, 0, 1, 2], 0) -> True
    """
    # TODO: Implement your solution here
    pass


def test_search():
    # Test cases
    assert search([2, 5, 6, 0, 0, 1, 2], 0) == True
    assert search([2, 5, 6, 0, 0, 1, 2], 3) == False
    assert search([1, 0, 1, 1, 1], 0) == True
    assert search([1, 1, 1, 1, 1], 2) == False
    assert search([1], 1) == True
    print("All test cases passed!")


if __name__ == "__main__":
    test_search()
