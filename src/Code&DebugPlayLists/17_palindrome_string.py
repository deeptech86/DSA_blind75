# #recursion #string
# Check if a String is Palindrome or Not
# Source: Code & Debug - DSA Python Course Part 17

def is_palindrome_string(s: str) -> bool:
    """
    Check if a string is a palindrome using recursion.

    Args:
        s: A string to check

    Returns:
        True if the string is a palindrome, False otherwise

    Example:
        is_palindrome_string("racecar") -> True
        is_palindrome_string("hello") -> False
    """
    # TODO: Implement your solution here
    if len(s)<=1:
        return True
    s=s.lower()
    r=len(s)-1
    l=0
    while l<r:
        if s[l]!=s[r]:
            return False
        l=l+1
        r=r-1
    return True







def test_is_palindrome_string():
    # Test cases
    assert is_palindrome_string("racecar") == True
    assert is_palindrome_string("hello") == False
    assert is_palindrome_string("a") == True
    assert is_palindrome_string("") == True
    assert is_palindrome_string("madam") == True
    assert is_palindrome_string("ab") == False
    print("All test cases passed!")


if __name__ == "__main__":
    test_is_palindrome_string()
