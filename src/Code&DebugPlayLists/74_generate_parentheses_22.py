# #backtracking #recursion
# LeetCode 22: Generate Parentheses
# Source: Code & Debug - DSA Python Course Part 74

from typing import List

def generate_parenthesis(n: int) -> List[str]:
    """
    Generate all combinations of well-formed parentheses.

    Args:
        n: Number of pairs of parentheses

    Returns:
        All valid combinations of n pairs of parentheses

    Example:
        generate_parenthesis(3) -> ["((()))", "(()())", "(())()", "()(())", "()()()"]
    """
    # TODO: Implement your solution here
    pass


def test_generate_parenthesis():
    # Test cases
    result1 = generate_parenthesis(3)
    expected1 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    assert sorted(result1) == sorted(expected1)

    result2 = generate_parenthesis(1)
    assert result2 == ["()"]

    result3 = generate_parenthesis(2)
    assert sorted(result3) == sorted(["(())", "()()"])

    print("All test cases passed!")


if __name__ == "__main__":
    test_generate_parenthesis()
