# #array #two_pointers #sorting
# LeetCode 18: 4Sum Problem
# Source: Code & Debug - DSA Python Course Part 45

from typing import List

def four_sum(nums: List[int], target: int) -> List[List[int]]:
    """
    Find all unique quadruplets that sum to target.

    Args:
        nums: A list of integers
        target: The target sum

    Returns:
        List of all unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
        that sum to target

    Example:
        four_sum([1, 0, -1, 0, -2, 2], 0) -> [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    """
    # TODO: Implement your solution here
    pass


def test_four_sum():
    # Test cases
    result1 = four_sum([1, 0, -1, 0, -2, 2], 0)
    expected1 = [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
    assert sorted([sorted(x) for x in result1]) == sorted([sorted(x) for x in expected1])

    result2 = four_sum([2, 2, 2, 2, 2], 8)
    assert result2 == [[2, 2, 2, 2]]

    result3 = four_sum([1, 2, 3, 4], 100)
    assert result3 == []

    print("All test cases passed!")


if __name__ == "__main__":
    test_four_sum()
