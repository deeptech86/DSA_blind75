# #recursion #backtracking
# Generate All Subsequences Using Recursion
# Source: Code & Debug - DSA Python Course Part 69

from typing import List

def generate_subsequences(arr: List[int]) -> List[List[int]]:
    """
    Generate all subsequences of an array using recursion.

    Args:
        arr: A list of integers

    Returns:
        All possible subsequences

    Example:
        generate_subsequences([1, 2, 3]) -> [[], [3], [2], [2,3], [1], [1,3], [1,2], [1,2,3]]
    """
    # TODO: Implement your solution here
    pass


def test_generate_subsequences():
    # Test cases
    result1 = generate_subsequences([1, 2, 3])
    assert len(result1) == 8
    assert [] in result1
    assert [1, 2, 3] in result1

    result2 = generate_subsequences([1])
    assert len(result2) == 2

    result3 = generate_subsequences([])
    assert result3 == [[]]

    print("All test cases passed!")


if __name__ == "__main__":
    test_generate_subsequences()
