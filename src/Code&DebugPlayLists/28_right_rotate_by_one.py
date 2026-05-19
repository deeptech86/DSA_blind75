# #array
# Right Rotate an Array by One Place
# Source: Code & Debug - DSA Python Course Part 28

from typing import List

def rotate_by_one(arr: List[int]) -> List[int]:
    """
    Right rotate an array by one place.

    Args:
        arr: A list of integers

    Returns:
        The rotated list

    Example:
        rotate_by_one([1, 2, 3, 4, 5]) -> [5, 1, 2, 3, 4]
    """
    # TODO: Implement your solution here
    pass


def test_rotate_by_one():
    # Test cases
    assert rotate_by_one([1, 2, 3, 4, 5]) == [5, 1, 2, 3, 4]
    assert rotate_by_one([1]) == [1]
    assert rotate_by_one([1, 2]) == [2, 1]
    assert rotate_by_one([]) == []
    assert rotate_by_one([9, 8, 7, 6]) == [6, 9, 8, 7]
    print("All test cases passed!")


if __name__ == "__main__":
    test_rotate_by_one()
