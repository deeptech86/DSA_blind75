# #array #dynamic_programming #kadane
# LeetCode 53: Find the Maximum Subarray Sum (Kadane's Algorithm)
# Source: Code & Debug - DSA Python Course Part 36

from typing import List

def max_subarray(nums: List[int]) -> int:
    """
    Find the contiguous subarray with the largest sum.

    Args:
        nums: A list of integers

    Returns:
        The maximum subarray sum

    Example:
        max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> 6
        (subarray [4, -1, 2, 1] has the largest sum = 6)
    """
    # TODO: Implement your solution here
    pass


def test_max_subarray():
    # Test cases
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    assert max_subarray([-1]) == -1
    assert max_subarray([-2, -1]) == -1
    print("All test cases passed!")


if __name__ == "__main__":
    test_max_subarray()
