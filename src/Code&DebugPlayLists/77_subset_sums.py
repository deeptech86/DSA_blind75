# #backtracking #recursion
# Subset Sums - GFG Problem
# Source: Code & Debug - DSA Python Course Part 77

from typing import List

def subset_sums(arr: List[int]) -> List[int]:
    """
    Return all possible subset sums in increasing order.

    Args:
        arr: A list of integers

    Returns:
        All possible subset sums sorted in increasing order

    Example:
        subset_sums([2, 3]) -> [0, 2, 3, 5]
    """
    # TODO: Implement your solution here
    pass


def test_subset_sums():
    # Test cases
    assert subset_sums([2, 3]) == [0, 2, 3, 5]
    assert subset_sums([5, 2, 1]) == [0, 1, 2, 3, 5, 6, 7, 8]
    assert subset_sums([1]) == [0, 1]
    assert subset_sums([]) == [0]
    print("All test cases passed!")


if __name__ == "__main__":
    test_subset_sums()
