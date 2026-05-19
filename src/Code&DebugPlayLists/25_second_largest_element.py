# #array
# Find the Second Largest Element in an Array Without Sorting
# Source: Code & Debug - DSA Python Course Part 25
import math
from typing import List

from more_itertools.more import first


def find_second_largest(arr: List[int]) -> int:
    """
    Find the second largest element in an array without sorting.

    Args:
        arr: A list of integers with at least 2 distinct elements

    Returns:
        The second largest element, or -1 if not found

    Example:
        find_second_largest([1, 8, 7, 56, 90]) -> 56
    """
    # TODO: Implement your solution here
    first=-float("inf")

    second=-math.inf
    for i in (arr):
        if i>=first :
            second=first
            first=i
        elif i!=first and i>second:
            second=i
    if first==second:
        return -1
    else:
        return second




def test_find_second_largest():
    # Test cases
    assert find_second_largest([-10,-2,-5])== -5
    assert find_second_largest([5, 5, 5]) == -1  # All same elements
    assert find_second_largest([1, 58, 7, 56, 90]) == 58
    assert find_second_largest([10, 20]) == 10

    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([100, 50, 75, 25]) == 75
    print("All test cases passed!")


if __name__ == "__main__":
    test_find_second_largest()
