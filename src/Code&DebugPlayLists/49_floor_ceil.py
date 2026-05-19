# #binary_search
# Floor & Ceil in Sorted Array
# Source: Code & Debug - DSA Python Course Part 49

from typing import List, Tuple

def find_floor_ceil(nums: List[int], target: int) -> Tuple[int, int]:
    """
    Find floor and ceil of target in a sorted array.
    Floor: Largest element <= target
    Ceil: Smallest element >= target

    Args:
        nums: A sorted list of integers
        target: The target value

    Returns:
        Tuple of (floor, ceil). -1 if not found.

    Example:
        find_floor_ceil([1, 2, 8, 10, 10, 12, 19], 5) -> (2, 8)
    """
    # TODO: Implement your solution here
    pass


def test_find_floor_ceil():
    # Test cases
    assert find_floor_ceil([1, 2, 8, 10, 10, 12, 19], 5) == (2, 8)
    assert find_floor_ceil([1, 2, 8, 10, 10, 12, 19], 10) == (10, 10)
    assert find_floor_ceil([1, 2, 8, 10, 10, 12, 19], 0) == (-1, 1)
    assert find_floor_ceil([1, 2, 8, 10, 10, 12, 19], 20) == (19, -1)
    assert find_floor_ceil([1, 2, 3], 2) == (2, 2)
    print("All test cases passed!")


if __name__ == "__main__":
    test_find_floor_ceil()
