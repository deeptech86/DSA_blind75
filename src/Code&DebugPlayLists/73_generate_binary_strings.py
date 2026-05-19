# #backtracking #recursion
# Generate All Binary Strings (No consecutive 1s) - GFG Problem
# Source: Code & Debug - DSA Python Course Part 73

from typing import List

def generate_binary_strings(n: int) -> List[str]:
    """
    Generate all binary strings of length n with no consecutive 1s.

    Args:
        n: Length of binary strings

    Returns:
        All valid binary strings

    Example:
        generate_binary_strings(3) -> ['000', '001', '010', '100', '101']
    """
    # TODO: Implement your solution here
    pass


def test_generate_binary_strings():
    # Test cases
    result1 = generate_binary_strings(3)
    assert sorted(result1) == sorted(['000', '001', '010', '100', '101'])

    result2 = generate_binary_strings(2)
    assert sorted(result2) == sorted(['00', '01', '10'])

    result3 = generate_binary_strings(1)
    assert sorted(result3) == sorted(['0', '1'])

    print("All test cases passed!")


if __name__ == "__main__":
    test_generate_binary_strings()
