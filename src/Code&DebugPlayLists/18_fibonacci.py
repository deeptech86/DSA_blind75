# #recursion #dynamic_programming
# Find the Fibonacci Number
# Source: Code & Debug - DSA Python Course Part 18

def fibonacci(n: int) -> int:
    """
    Find the nth Fibonacci number.
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(
    n-2)

    Args:
        n: A non-negative integer

    Returns:
        The nth Fibonacci number

    Example:
        fibonacci(6) -> 8 (0, 1, 1, 2, 3, 5, 8)
    """
    # TODO: Implement your solution here
    if (n==0):
        return 0
    if (n==1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)



def test_fibonacci():
    # Test cases
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(6) == 8
    assert fibonacci(10) == 55
    assert fibonacci(15) == 610
    print("All test cases passed!")


if __name__ == "__main__":
    test_fibonacci()
