# #binary_search
# Introduction to Binary Search
# Source: Code & Debug - DSA Python Course Part 46

from typing import List

def binary_search(nums: List[int], target: int) -> int:
    """
    Search for target in a sorted array using binary search.
    Time Complexity: O(log n)

    Args:
        nums: A sorted list of integers
        target: The element to search for

    Returns:
        Index of target if found, -1 otherwise

    Example:
        binary_search([1, 2, 3, 4, 5], 3) -> 2
    """
    # TODO: Implement your solution here
    pass


def test_binary_search():
    # Test cases
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
    assert binary_search([5], 5) == 0
    assert binary_search([], 1) == -1
    print("All test cases passed!")


if __name__ == "__main__":
    test_binary_search()
