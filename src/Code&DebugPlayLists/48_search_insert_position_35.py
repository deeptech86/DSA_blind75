# #binary_search
# LeetCode 35: Search Insert Position
# Source: Code & Debug - DSA Python Course Part 48

from typing import List

def search_insert(nums: List[int], target: int) -> int:
    """
    Find the index where target should be inserted to keep array sorted.

    Args:
        nums: A sorted list of distinct integers
        target: The target value

    Returns:
        Index of target or where it would be inserted

    Example:
        search_insert([1, 3, 5, 6], 5) -> 2
        search_insert([1, 3, 5, 6], 2) -> 1
    """
    # TODO: Implement your solution here
    pass


def test_search_insert():
    # Test cases
    assert search_insert([1, 3, 5, 6], 5) == 2
    assert search_insert([1, 3, 5, 6], 2) == 1
    assert search_insert([1, 3, 5, 6], 7) == 4
    assert search_insert([1, 3, 5, 6], 0) == 0
    assert search_insert([1], 0) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    test_search_insert()
