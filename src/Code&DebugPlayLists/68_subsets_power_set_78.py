# #bit_manipulation #backtracking
# LeetCode 78: Generate Subsets / Power Set
# Source: Code & Debug - DSA Python Course Part 68

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    """
    Generate all possible subsets (the power set) using bit manipulation.

    Args:
        nums: A list of unique integers

    Returns:
        All possible subsets

    Example:
        subsets([1, 2, 3]) -> [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
    """
    # TODO: Implement your solution here
    pass


def test_subsets():
    # Test cases
    result1 = subsets([1, 2, 3])
    assert len(result1) == 8
    assert [] in result1
    assert [1, 2, 3] in result1

    result2 = subsets([0])
    assert sorted(result2) == sorted([[], [0]])

    result3 = subsets([1, 2])
    assert len(result3) == 4
    assert sorted([sorted(x) for x in result3]) == sorted([[], [1], [2], [1, 2]])

    print("All test cases passed!")


if __name__ == "__main__":
    test_subsets()
