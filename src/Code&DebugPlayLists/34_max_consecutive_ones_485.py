# #array
# LeetCode 485: Max Consecutive Ones
# Source: Code & Debug - DSA Python Course Part 34

from typing import List

def find_max_consecutive_ones(nums: List[int]) -> int:
    """
    Find the maximum number of consecutive 1's in a binary array.

    Args:
        nums: A binary array (contains only 0s and 1s)

    Returns:
        Maximum number of consecutive 1's

    Example:
        find_max_consecutive_ones([1, 1, 0, 1, 1, 1]) -> 3
    """
    # TODO: Implement your solution here
    pass


def test_find_max_consecutive_ones():
    # Test cases
    assert find_max_consecutive_ones([0, 1, 1, 0, 1, 1, 1]) == 3
    assert find_max_consecutive_ones([1, 0, 1, 1, 0, 1]) == 2
    assert find_max_consecutive_ones([0, 0, 0]) == 0
    assert find_max_consecutive_ones([1, 1, 1, 1]) == 4
    assert find_max_consecutive_ones([1]) == 1
    print("All test cases passed!")


if __name__ == "__main__":
    test_find_max_consecutive_ones()
