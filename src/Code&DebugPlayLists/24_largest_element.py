# #array
# Find the Largest Element in an Array
# Source: Code & Debug - DSA Python Course Part 24

from typing import List

def find_largest(arr: List[int]) -> int:
    """
    Find the largest element in an array.

    Args:
        arr: A non-empty list of integers

    Returns:
        The largest element in the array

    Example:
        find_largest([1, 8, 7, 56, 90]) -> 90
    """
    # TODO: Implement your solution here
    pass


def test_find_largest():
    # Test cases
    assert find_largest([1, 8, 7, 56, 90]) == 90
    assert find_largest([1]) == 1
    assert find_largest([5, 5, 5]) == 5
    assert find_largest([-1, -5, -2]) == -1
    assert find_largest([10, 20, 30, 40, 50]) == 50
    print("All test cases passed!")


if __name__ == "__main__":
    test_find_largest()
