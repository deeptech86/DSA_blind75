# #sorting #divide_and_conquer
# Quick Sort Algorithm in Python
# Source: Code & Debug - DSA Python Course Part 23

from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    """
    Sort an array using Quick Sort algorithm (Divide and Conquer).
    Time Complexity: O(n log n) average, O(n^2) worst case
    Space Complexity: O(log n)

    Args:
        arr: A list of integers

    Returns:
        The sorted list

    Example:
        quick_sort([10, 7, 8, 9, 1, 5]) -> [1, 5, 7, 8, 9, 10]
    """
    # TODO: Implement your solution here
    pass


def test_quick_sort():
    # Test cases
    assert quick_sort([10, 7, 8, 9, 1, 5]) == [1, 5, 7, 8, 9, 10]
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert quick_sort([1]) == [1]
    assert quick_sort([]) == []
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert quick_sort([3, 3, 3]) == [3, 3, 3]
    print("All test cases passed!")


if __name__ == "__main__":
    test_quick_sort()
