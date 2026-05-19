# #array
# Check if an Array is Sorted
# Source: Code & Debug - DSA Python Course Part 26

from typing import List

def is_sorted(arr: List[int]) -> bool:
    """
    Check if an array is sorted in non-decreasing order.

    Args:
        arr: A list of integers

    Returns:
        True if sorted, False otherwise

    Example:
        is_sorted([1, 2, 3, 4, 5]) -> True
        is_sorted([1, 3, 2, 4, 5]) -> False
    """
    # TODO: Implement your solution here

    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True




def test_is_sorted():
    # Test cases
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 3, 2, 4, 5]) == False
    assert is_sorted([1]) == True
    assert is_sorted([]) == True
    assert is_sorted([1, 1, 1, 1]) == True
    assert is_sorted([5, 4, 3, 2, 1]) == False
    print("All test cases passed!")


if __name__ == "__main__":
    test_is_sorted()
