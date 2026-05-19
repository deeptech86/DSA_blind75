# #array #two_pointers #sorting
# LeetCode 15: 3Sum Problem
# Source: Code & Debug - DSA Python Course Part 44

from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets that sum to zero.

    Args:
        nums: A list of integers

    Returns:
        List of all unique triplets [nums[i], nums[j], nums[k]]
        where nums[i] + nums[j] + nums[k] == 0

    Example:
        three_sum([-1, 0, 1, 2, -1, -4]) -> [[-1, -1, 2], [-1, 0, 1]]
    """
    # TODO: Implement your solution here
    pass


def test_three_sum():
    # Test cases
    result1 = three_sum([-1, 0, 1, 2, -1, -4])
    assert sorted([sorted(x) for x in result1]) == sorted([[-1, -1, 2], [-1, 0, 1]])

    result2 = three_sum([0, 1, 1])
    assert result2 == []

    result3 = three_sum([0, 0, 0])
    assert result3 == [[0, 0, 0]]

    print("All test cases passed!")


if __name__ == "__main__":
    test_three_sum()
