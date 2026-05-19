# #basics #math
# Count the Number of Digits in an Integer
# Source: Code & Debug - DSA Python Course Part 6
import math

def count_digits(n: int) -> int:
    """
    Count the number of digits in a given integer.

    Args:
        n: An integer (can be positive or negative)

    Returns:
        The number of digits in the integer

    Example:
        count_digits(12345) -> 5
        count_digits(-123) -> 3
    """
    # TODO: Implement your solution here
    nums=n
    digit=0
    if nums == 0:
        return 1
    nums=abs(nums)
    while nums>0:
            remainder = nums%10
            digit +=1
            nums=nums//10
    return digit
    # print (int(math.log10(n)+1))
    # return int(math.log10(n)+1)




def test_count_digits():
    # Test cases
    assert count_digits(12345) == 5
    assert count_digits(0) == 1
    assert count_digits(9) == 1
    assert count_digits(-123) == 3
    assert count_digits(1000000) == 7
    print("All test cases passed!")


if __name__ == "__main__":
    test_count_digits()
