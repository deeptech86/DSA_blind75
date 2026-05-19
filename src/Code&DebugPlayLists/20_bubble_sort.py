# #sorting
# Bubble Sort in Python
# Source: Code & Debug - DSA Python Course Part 20

from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Sort an array using Bubble Sort algorithm.
    Time Complexity: O(n^2)
    Space Complexity: O(1)

    Args:
        arr: A list of integers

    Returns:
        The sorted list

    Example:
        bubble_sort([64, 34, 25, 12, 22]) -> [12, 22, 25, 34, 64]
    """
    # TODO: Implement your solution here
    pass


def test_bubble_sort():
    # Test cases
    assert bubble_sort([64, 34, 25, 12, 22]) == [12, 22, 25, 34, 64]
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([1]) == [1]
    assert bubble_sort([]) == []
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([3, 3, 3]) == [3, 3, 3]
    print("All test cases passed!")


if __name__ == "__main__":
    test_bubble_sort()
