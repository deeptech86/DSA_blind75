# #backtracking #recursion
# LeetCode 40: Combination Sum II
# Source: Code & Debug - DSA Python Course Part 76

from typing import List

def combination_sum2(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations that sum to target.
    Each number can only be used once.

    Args:
        candidates: Collection of integers (may contain duplicates)
        target: Target sum

    Returns:
        All unique combinations summing to target

    Example:
        combination_sum2([10, 1, 2, 7, 6, 1, 5], 8) -> [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    """
    # TODO: Implement your solution here
    pass


def test_combination_sum2():
    # Test cases
    result1 = combination_sum2([10, 1, 2, 7, 6, 1, 5], 8)
    expected1 = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    assert sorted([sorted(x) for x in result1]) == sorted([sorted(x) for x in expected1])

    result2 = combination_sum2([2, 5, 2, 1, 2], 5)
    expected2 = [[1, 2, 2], [5]]
    assert sorted([sorted(x) for x in result2]) == sorted([sorted(x) for x in expected2])

    print("All test cases passed!")


if __name__ == "__main__":
    test_combination_sum2()
