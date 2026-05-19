# #recursion #backtracking
# Generate Subsequences with Sum K
# Source: Code & Debug - DSA Python Course Part 70

from typing import List

def subsequences_with_sum(arr: List[int], k: int) -> List[List[int]]:
    """
    Generate all subsequences whose elements sum to k.

    Args:
        arr: A list of integers
        k: Target sum

    Returns:
        All subsequences that sum to k

    Example:
        subsequences_with_sum([1, 2, 1], 2) -> [[1, 1], [2]]
    """
    # TODO: Implement your solution here
    pass


def test_subsequences_with_sum():
    # Test cases
    result1 = subsequences_with_sum([1, 2, 1], 2)
    assert [1, 1] in result1 or sorted([1, 1]) in [sorted(x) for x in result1]
    assert [2] in result1

    result2 = subsequences_with_sum([1, 2, 3], 3)
    assert [3] in result2
    assert [1, 2] in result2

    result3 = subsequences_with_sum([1, 2, 3], 10)
    assert result3 == []

    print("All test cases passed!")


if __name__ == "__main__":
    test_subsequences_with_sum()
