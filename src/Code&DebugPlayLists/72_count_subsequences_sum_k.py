# #backtracking #recursion
# Count All Subsequences with Sum K
# Source: Code & Debug - DSA Python Course Part 72

from typing import List

def count_subsequences_with_sum(arr: List[int], k: int) -> int:
    """
    Count all subsequences whose elements sum to k.

    Args:
        arr: A list of positive integers
        k: Target sum

    Returns:
        Number of subsequences that sum to k

    Example:
        count_subsequences_with_sum([1, 2, 1], 2) -> 2 (subsequences: [1,1], [2])
    """
    # TODO: Implement your solution here
    pass


def test_count_subsequences_with_sum():
    # Test cases
    assert count_subsequences_with_sum([1, 2, 1], 2) == 2
    assert count_subsequences_with_sum([1, 2, 3], 3) == 2
    assert count_subsequences_with_sum([1, 1, 1, 1], 2) == 6
    assert count_subsequences_with_sum([1, 2, 3], 10) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    test_count_subsequences_with_sum()
