# #binary_search
# LeetCode 34: Find First & Last Occurrence in Sorted Array
# Source: Code & Debug - DSA Python Course Part 50

from typing import List

def search_range(nums: List[int], target: int) -> List[int]:
    """
    Find the starting and ending position of target in sorted array.

    Args:
        nums: A sorted list of integers
        target: The target value

    Returns:
        [first_index, last_index] or [-1, -1] if not found

    Example:
        search_range([5, 7, 7, 8, 8, 10], 8) -> [3, 4]
    """
    # TODO: Implement your solution here
    pass


def test_search_range():
    # Test cases
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert search_range([], 0) == [-1, -1]
    assert search_range([1], 1) == [0, 0]
    assert search_range([2, 2], 2) == [0, 1]
    print("All test cases passed!")


if __name__ == "__main__":
    test_search_range()
