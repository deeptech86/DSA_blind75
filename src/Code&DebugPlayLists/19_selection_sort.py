# #sorting
# Selection Sort in Python
# Source: Code & Debug - DSA Python Course Part 19

from typing import List

def selection_sort(arr: List[int]) -> List[int]:
    """
    Sort an array using Selection Sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Args:
        arr: A list of integers

    Returns:
        The sorted list

    Example:
        selection_sort([64, 25, 12, 22, 11]) -> [11, 12, 22, 25, 64]
    """
    # TODO: Implement your solution here
    pass


def test_selection_sort():
    # Test cases
    assert selection_sort([64, 25, 12, 22, 11]) == [11, 12, 22, 25, 64]
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert selection_sort([1]) == [1]
    assert selection_sort([]) == []
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert selection_sort([3, 3, 3]) == [3, 3, 3]
    print("All test cases passed!")


if __name__ == "__main__":
    test_selection_sort()
