# #array #math #bit_manipulation
# LeetCode 268: Find Missing Number in an Array
# Source: Code & Debug - DSA Python Course Part 33

from typing import List

def missing_number(nums: List[int]) -> int:
    """
    Find the missing number in an array containing n distinct numbers
    from the range [0, n].

    Args:
        nums: A list of n distinct integers in range [0, n]

    Returns:
        The missing number

    Example:
        missing_number([3, 0, 1]) -> 2
    """
    # TODO: Implement your solution here
    nums.sort()
    for i in range(len(nums)):
        if nums[i]!=i:
            return i



def test_missing_number():
    # Test cases
    assert missing_number([3, 0, 1]) == 2
    assert missing_number([0, 1]) == 2
    assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert missing_number([0]) == 1
    assert missing_number([1]) == 0
    print("All test cases passed!")


if __name__ == "__main__":
    test_missing_number()
