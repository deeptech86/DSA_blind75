# #backtracking #recursion
# LeetCode 216: Combination Sum III
# Source: Code & Debug - DSA Python Course Part 78

from typing import List

def combination_sum3(k: int, n: int) -> List[List[int]]:
    """
    Find all valid combinations of k numbers (1-9) that sum to n.
    Each number can only be used once.

    Args:
        k: Number of elements in combination
        n: Target sum

    Returns:
        All valid combinations

    Example:
        combination_sum3(3, 7) -> [[1, 2, 4]]
    """
    # TODO: Implement your solution here
    pass


def test_combination_sum3():
    # Test cases
    assert combination_sum3(3, 7) == [[1, 2, 4]]

    result2 = combination_sum3(3, 9)
    expected2 = [[1, 2, 6], [1, 3, 5], [2, 3, 4]]
    assert sorted([sorted(x) for x in result2]) == sorted([sorted(x) for x in expected2])

    assert combination_sum3(4, 1) == []
    assert combination_sum3(2, 3) == [[1, 2]]

    print("All test cases passed!")


if __name__ == "__main__":
    test_combination_sum3()
