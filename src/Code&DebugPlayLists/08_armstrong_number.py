# #basics #math
# Armstrong Number
# Source: Code & Debug - DSA Python Course Part 8
from numpy.ma.core import remainder


def is_armstrong(n: int) -> bool:
    """
    Check if a number is an Armstrong number.
    An Armstrong number is a number that is equal to the sum of
    its own digits each raised to the power of the number of digits.

    Args:
        n: A positive integer to check

    Returns:
        True if the number is an Armstrong number, False otherwise

    Example:
        is_armstrong(153) -> True  (1^3 + 5^3 + 3^3 = 153)
        is_armstrong(123) -> False
    """
    # TODO: Implement your solution here
    result = 0
    length= len(str(n))
    if length==1:
        return True
    nums=n

    while nums>0:
        remainder=nums%10
        result+=(remainder**length)
        nums=nums//10
    return result==n



def test_is_armstrong():
    # Test cases
    assert is_armstrong(153) == True   # 1^3 + 5^3 + 3^3 = 153
    assert is_armstrong(370) == True   # 3^3 + 7^3 + 0^3 = 370
    assert is_armstrong(371) == True   # 3^3 + 7^3 + 1^3 = 371
    assert is_armstrong(407) == True   # 4^3 + 0^3 + 7^3 = 407
    assert is_armstrong(123) == False
    assert is_armstrong(1) == True     # Single digit numbers are Armstrong
    assert is_armstrong(9) == True
    print("All test cases passed!")


if __name__ == "__main__":
    test_is_armstrong()
