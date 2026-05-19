# #sorting #divide_and_conquer
# Merge Sort in Python
# Source: Code & Debug - DSA Python Course Part 22

from typing import List

def merge_sort(arr: List[int]) -> List[int]:
    """
    Sort an array using Merge Sort algorithm (Divide and Conquer).
    Time Complexity: O(n log n)
    Space Complexity: O(n)

    Args:
        arr: A list of integers

    Returns:
        The sorted list

    Example:
        merge_sort([38, 27, 43, 3, 9, 82, 10]) -> [3, 9, 10, 27, 38, 43, 82]
    """
    # TODO: Implement your solution here
    pass


def test_merge_sort():
    # Test cases
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort([1]) == [1]
    assert merge_sort([]) == []
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([3, 3, 3]) == [3, 3, 3]
    print("All test cases passed!")


if __name__ == "__main__":
    test_merge_sort()
