# #basics #math
# Check if a Number is Palindrome or Not
# Source: Code & Debug - DSA Python Course Part 7

def is_palindrome_number(n: int) -> bool:
    """
    Check if a number is a palindrome.
    A palindrome number reads the same backward as forward.

    Args:
        n: An integer to check

    Returns:
        True if the number is a palindrome, False otherwise

    Example:
        is_palindrome_number(121) -> True
        is_palindrome_number(123) -> False
    """
    # TODO: Implement your solution here
    nums=n
    result=0
    if nums<10 and nums>=0:
        return True
    while nums>0:
        remainder = nums%10

        result= result*10 +remainder
        nums = nums // 10
    return result==n





def test_is_palindrome_number():
    # Test cases
    assert is_palindrome_number(121) == True
    assert is_palindrome_number(12321) == True
    assert is_palindrome_number(123) == False
    assert is_palindrome_number(-121) == False  # Negative numbers are not palindromes
    assert is_palindrome_number(0) == True
    assert is_palindrome_number(10) == False
    print("All test cases passed!")


if __name__ == "__main__":
    test_is_palindrome_number()
