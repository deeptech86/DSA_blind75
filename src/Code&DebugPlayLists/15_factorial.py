# #recursion #math
# Find the Factorial of a Number
# Source: Code & Debug - DSA Python Course Part 15

def factorial(n: int) -> int:
    """
    Calculate the factorial of a number using recursion.

    Args:
        n: A non-negative integer

    Returns:
        The factorial of n (n!)

    Example:
        factorial(5) -> 120 (5! = 5*4*3*2*1)
    """
    # TODO: Implement your solution here
    result=1
    if n==0 or n==1:
        return 1
    return n* factorial(n-1)


def test_factorial():
    # Test cases
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(10) == 3628800
    assert factorial(3) == 6
    print("All test cases passed!")


if __name__ == "__main__":
    test_factorial()
