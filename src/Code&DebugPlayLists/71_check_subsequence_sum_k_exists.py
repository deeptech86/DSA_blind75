# #backtracking
# Check if a Subsequence with Sum = K Exists
# Source: Code & Debug - DSA Python Course Part 71

from typing import List

def has_subsequence_with_sum(arr: List[int], k: int) -> bool:
    """
    Check if there exists a subsequence with sum equal to k.

    Args:
        arr: A list of integers
        k: Target sum

    Returns:
        True if such subsequence exists, False otherwise

    Example:
        has_subsequence_with_sum([1, 2, 3], 5) -> True (subsequence [2, 3])
    """
    # TODO: Implement your solution here
    pass


def test_has_subsequence_with_sum():
    # Test cases
    assert has_subsequence_with_sum([1, 2, 3], 5) == True
    assert has_subsequence_with_sum([1, 2, 3], 6) == True
    assert has_subsequence_with_sum([1, 2, 3], 10) == False
    assert has_subsequence_with_sum([1, 2, 3], 0) == True  # Empty subsequence
    assert has_subsequence_with_sum([], 0) == True
    print("All test cases passed!")


if __name__ == "__main__":
    test_has_subsequence_with_sum()
