# #stack #monotonic_stack
# LeetCode 503: Next Greater Element II (Circular Array)
# Source: Code & Debug - DSA Python Course Part 92

from typing import List

def next_greater_elements(nums: List[int]) -> List[int]:
    """
    Find the next greater element for each element in a circular array.
    The array is treated as circular (last element's next is first element).

    Args:
        nums: A circular array of integers

    Returns:
        List where result[i] is the next greater element of nums[i],
        or -1 if no such element exists

    Example:
        next_greater_elements([1, 2, 1]) -> [2, -1, 2]
    """
    # TODO: Implement your solution here
    pass


def test_next_greater_elements():
    # Test cases
    assert next_greater_elements([1, 2, 1]) == [2, -1, 2]
    assert next_greater_elements([1, 2, 3, 4, 3]) == [2, 3, 4, -1, 4]
    assert next_greater_elements([5, 4, 3, 2, 1]) == [-1, 5, 5, 5, 5]
    assert next_greater_elements([1, 1, 1, 1]) == [-1, -1, -1, -1]
    assert next_greater_elements([1]) == [-1]
    print("All test cases passed!")


if __name__ == "__main__":
    test_next_greater_elements()
