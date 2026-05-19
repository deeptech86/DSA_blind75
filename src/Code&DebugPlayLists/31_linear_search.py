# #array #searching
# Implementing Linear Search
# Source: Code & Debug - DSA Python Course Part 31

from typing import List

def linear_search(arr: List[int], target: int) -> int:
    """
    Search for a target element in an array using linear search.

    Args:
        arr: A list of integers
        target: The element to search for

    Returns:
        Index of target if found, -1 otherwise

    Example:
        linear_search([1, 2, 3, 4, 5], 3) -> 2
    """
    # TODO: Implement your solution here
    pass


def test_linear_search():
    # Test cases
    assert linear_search([1, 2, 3, 4, 5], 3) == 2
    assert linear_search([1, 2, 3, 4, 5], 6) == -1
    assert linear_search([5], 5) == 0
    assert linear_search([], 1) == -1
    assert linear_search([1, 1, 1, 1], 1) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    test_linear_search()
