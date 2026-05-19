# #bit_manipulation #array
# LeetCode 136: Single Number (XOR Trick)
# Source: Code & Debug - DSA Python Course Part 67

from typing import List

def single_number(nums: List[int]) -> int:
    """
    Find the element that appears only once (all others appear twice).
    Must use constant extra space.

    Args:
        nums: A list where every element appears twice except one

    Returns:
        The single element

    Example:
        single_number([2, 2, 1]) -> 1
    """
    # TODO: Implement your solution here
    pass


def test_single_number():
    # Test cases
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1
    assert single_number([1, 1, 2, 2, 3]) == 3
    print("All test cases passed!")


if __name__ == "__main__":
    test_single_number()
