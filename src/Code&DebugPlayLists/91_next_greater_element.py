# #stack #monotonic_stack
# Next Greater Element (Monotonic Stack Approach) - GFG Problem
# Source: Code & Debug - DSA Python Course Part 91

from typing import List

def next_greater_element(arr: List[int]) -> List[int]:
    """
    Find the next greater element for each element in the array.
    The next greater element of an element x is the first element
    to its right that is greater than x.

    Args:
        arr: A list of integers

    Returns:
        List where result[i] is the next greater element of arr[i],
        or -1 if no such element exists

    Example:
        next_greater_element([4, 5, 2, 25]) -> [5, 25, 25, -1]
    """
    # TODO: Implement your solution here
    pass


def test_next_greater_element():
    # Test cases
    assert next_greater_element([4, 5, 2, 25]) == [5, 25, 25, -1]
    assert next_greater_element([13, 7, 6, 12]) == [-1, 12, 12, -1]
    assert next_greater_element([1, 2, 3, 4]) == [2, 3, 4, -1]
    assert next_greater_element([4, 3, 2, 1]) == [-1, -1, -1, -1]
    assert next_greater_element([1]) == [-1]
    print("All test cases passed!")


if __name__ == "__main__":
    test_next_greater_element()
