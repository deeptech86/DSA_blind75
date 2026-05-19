# #binary_search
# Implementation of Lower and Upper Bound
# Source: Code & Debug - DSA Python Course Part 47

from typing import List

def lower_bound(nums: List[int], target: int) -> int:
    """
    Find the index of the first element >= target.

    Args:
        nums: A sorted list of integers
        target: The target value

    Returns:
        Index of first element >= target, or len(nums) if not found

    Example:
        lower_bound([1, 2, 4, 4, 5], 4) -> 2
    """
    # TODO: Implement your solution here
    pass


def upper_bound(nums: List[int], target: int) -> int:
    """
    Find the index of the first element > target.

    Args:
        nums: A sorted list of integers
        target: The target value

    Returns:
        Index of first element > target, or len(nums) if not found

    Example:
        upper_bound([1, 2, 4, 4, 5], 4) -> 4
    """
    # TODO: Implement your solution here
    pass


def test_bounds():
    # Test cases for lower_bound
    assert lower_bound([1, 2, 4, 4, 5], 4) == 2
    assert lower_bound([1, 2, 4, 4, 5], 3) == 2
    assert lower_bound([1, 2, 4, 4, 5], 6) == 5
    assert lower_bound([1, 2, 4, 4, 5], 0) == 0

    # Test cases for upper_bound
    assert upper_bound([1, 2, 4, 4, 5], 4) == 4
    assert upper_bound([1, 2, 4, 4, 5], 3) == 2
    assert upper_bound([1, 2, 4, 4, 5], 5) == 5
    assert upper_bound([1, 2, 4, 4, 5], 0) == 0

    print("All test cases passed!")


if __name__ == "__main__":
    test_bounds()
