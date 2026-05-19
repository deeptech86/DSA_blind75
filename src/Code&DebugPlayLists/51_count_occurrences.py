# #binary_search
# Count Occurrences in Sorted Array
# Source: Code & Debug - DSA Python Course Part 51

from typing import List

def count_occurrences(nums: List[int], target: int) -> int:
    """
    Count the number of occurrences of target in a sorted array.

    Args:
        nums: A sorted list of integers
        target: The target value

    Returns:
        Number of times target appears in the array

    Example:
        count_occurrences([1, 1, 2, 2, 2, 2, 3], 2) -> 4
    """
    # TODO: Implement your solution here
    pass


def test_count_occurrences():
    # Test cases
    assert count_occurrences([1, 1, 2, 2, 2, 2, 3], 2) == 4
    assert count_occurrences([1, 1, 2, 2, 2, 2, 3], 4) == 0
    assert count_occurrences([1, 1, 1, 1], 1) == 4
    assert count_occurrences([1, 2, 3, 4, 5], 3) == 1
    assert count_occurrences([], 1) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    test_count_occurrences()
