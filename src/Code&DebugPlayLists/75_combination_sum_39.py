# #backtracking #recursion
# LeetCode 39: Combination Sum
# Source: Code & Debug - DSA Python Course Part 75

from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations that sum to target.
    Same number can be used unlimited times.

    Args:
        candidates: List of distinct integers
        target: Target sum

    Returns:
        All unique combinations summing to target

    Example:
        combination_sum([2, 3, 6, 7], 7) -> [[2, 2, 3], [7]]
    """
    # TODO: Implement your solution here
    pass


def test_combination_sum():
    # Test cases
    result1 = combination_sum([2, 3, 6, 7], 7)
    assert sorted([sorted(x) for x in result1]) == sorted([[2, 2, 3], [7]])

    result2 = combination_sum([2, 3, 5], 8)
    assert sorted([sorted(x) for x in result2]) == sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])

    result3 = combination_sum([2], 1)
    assert result3 == []

    print("All test cases passed!")


if __name__ == "__main__":
    test_combination_sum()
