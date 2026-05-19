# #array #hashing
# LeetCode 1: Two Sum Problem
# Source: Code & Debug - DSA Python Course Part 35

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target and return their indices.

    Args:
        nums: A list of integers
        target: The target sum

    Returns:
        Indices of the two numbers that add up to target

    Example:
        two_sum([2, 7, 11, 15], 9) -> [0, 1]
    """
    # TODO: Implement your solution here
    pass


def test_two_sum():
    # Test cases
    result1 = two_sum([2, 7, 11, 15], 9)
    assert sorted(result1) == [0, 1]

    result2 = two_sum([3, 2, 4], 6)
    assert sorted(result2) == [1, 2]

    result3 = two_sum([3, 3], 6)
    assert sorted(result3) == [0, 1]

    print("All test cases passed!")


if __name__ == "__main__":
    test_two_sum()
