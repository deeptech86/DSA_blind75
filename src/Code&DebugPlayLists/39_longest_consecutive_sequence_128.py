# #array #hashing
# LeetCode 128: Longest Consecutive Sequence
# Source: Code & Debug - DSA Python Course Part 39

from typing import List

def longest_consecutive(nums: List[int]) -> int:
    """
    Find the length of the longest consecutive elements sequence.
    Must run in O(n) time.

    Args:
        nums: An unsorted array of integers

    Returns:
        Length of the longest consecutive sequence

    Example:
        longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
        (The sequence is [1, 2, 3, 4])
    """
    # TODO: Implement your solution here
    pass


def test_longest_consecutive():
    # Test cases
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    assert longest_consecutive([1]) == 1
    assert longest_consecutive([1, 2, 0, 1]) == 3
    print("All test cases passed!")


if __name__ == "__main__":
    test_longest_consecutive()
