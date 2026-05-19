# #recursion #array
# Reverse an Array Using Recursion
# Source: Code & Debug - DSA Python Course Part 16

from typing import List

def reverse_array(arr: List[int]) -> List[int]:
    """
    Reverse an array using recursion.

    Args:
        arr: A list of integers

    Returns:
        The reversed list

    Example:
        reverse_array([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
    """
    # TODO: Implement your solution here
    if len(arr)==1:
        return arr

    l=0
    r=len(arr)-1
    while (l<r):
        arr[l],arr[r]=arr[r],arr[l]
        l=l+1
        r=r-1
    return arr



def test_reverse_array():
    # Test cases
    assert reverse_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_array([1]) == [1]
    assert reverse_array([]) == []
    assert reverse_array([1, 2]) == [2, 1]
    assert reverse_array([1, 2, 3]) == [3, 2, 1]
    print("All test cases passed!")


if __name__ == "__main__":
    test_reverse_array()
