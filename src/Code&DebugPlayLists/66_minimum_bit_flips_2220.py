# #bit_manipulation
# LeetCode 2220: Minimum Bit Flips to Convert Number
# Source: Code & Debug - DSA Python Course Part 66

def min_bit_flips(start: int, goal: int) -> int:
    """
    Find the minimum number of bit flips to convert start to goal.

    Args:
        start: Starting integer
        goal: Target integer

    Returns:
        Minimum number of bit flips required

    Example:
        min_bit_flips(10, 7) -> 3
        (10 = 1010, 7 = 0111, need to flip 3 bits)
    """
    # TODO: Implement your solution here
    pass


def test_min_bit_flips():
    # Test cases
    assert min_bit_flips(10, 7) == 3
    assert min_bit_flips(3, 4) == 3
    assert min_bit_flips(0, 0) == 0
    assert min_bit_flips(1, 1) == 0
    assert min_bit_flips(8, 0) == 1
    print("All test cases passed!")


if __name__ == "__main__":
    test_min_bit_flips()
