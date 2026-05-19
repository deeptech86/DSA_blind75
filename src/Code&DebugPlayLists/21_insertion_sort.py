# #sorting
# Insertion Sort in Python
# Source: Code & Debug - DSA Python Course Part 21

from typing import List

def insertion_sort(arr: List[int]) -> List[int]:
    """
    Sort an array using Insertion Sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Args:
        arr: A list of integers

    Returns:
        The sorted list

    Example:
        insertion_sort([12, 11, 13, 5, 6]) -> [5, 6, 11, 12, 13]
    """
    # TODO: Implement your solution here
    pass


def test_insertion_sort():
    # Test cases
    assert insertion_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13]
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert insertion_sort([1]) == [1]
    assert insertion_sort([]) == []
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert insertion_sort([3, 3, 3]) == [3, 3, 3]
    print("All test cases passed!")


if __name__ == "__main__":
    test_insertion_sort()
