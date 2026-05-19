# #stack
# LeetCode 20: Valid Parentheses
# Source: Code & Debug - DSA Python Course Part 88

def is_valid(s: str) -> bool:
    """
    Check if the input string has valid parentheses.
    Valid: (), [], {}, and proper nesting like ([{}])

    Args:
        s: String containing only '(){}[]'

    Returns:
        True if valid, False otherwise

    Example:
        is_valid("()[]{}") -> True
        is_valid("(]") -> False
    """
    # TODO: Implement your solution here
    pass


def test_is_valid():
    # Test cases
    assert is_valid("()") == True
    assert is_valid("()[]{}") == True
    assert is_valid("(]") == False
    assert is_valid("([)]") == False
    assert is_valid("{[]}") == True
    assert is_valid("") == True
    assert is_valid("(") == False
    print("All test cases passed!")


if __name__ == "__main__":
    test_is_valid()
