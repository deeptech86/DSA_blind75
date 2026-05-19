# #array
# LeetCode 2149: Rearrange Array Elements by Sign
# Source: Code & Debug - DSA Python Course Part 38

from typing import List

def rearrange_by_sign(nums: List[int]) -> List[int]:
    """
    Rearrange array so that positive and negative integers alternate.
    First element should be positive.
    Maintain relative order of positive and negative integers.

    Args:
        nums: A list with equal number of positive and negative integers

    Returns:
        Rearranged array with alternating positive/negative values

    Example:
        rearrange_by_sign([3, 1, -2, -5, 2, -4]) -> [3, -2, 1, -5, 2, -4]
    """
    # TODO: Implement your solution here
    pass


def test_rearrange_by_sign():
    # Test cases
    assert rearrange_by_sign([3, 1, -2, -5, 2, -4]) == [3, -2, 1, -5, 2, -4]
    assert rearrange_by_sign([-1, 1]) == [1, -1]
    assert rearrange_by_sign([1, -1]) == [1, -1]
    assert rearrange_by_sign([1, 2, -3, -4]) == [1, -3, 2, -4]
    print("All test cases passed!")


if __name__ == "__main__":
    test_rearrange_by_sign()
