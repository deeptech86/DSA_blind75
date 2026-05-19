# #backtracking #recursion
# LeetCode 17: Letter Combinations of a Phone Number
# Source: Code & Debug - DSA Python Course Part 79

from typing import List

def letter_combinations(digits: str) -> List[str]:
    """
    Return all possible letter combinations from phone digits.

    Phone mapping:
    2: abc, 3: def, 4: ghi, 5: jkl, 6: mno, 7: pqrs, 8: tuv, 9: wxyz

    Args:
        digits: A string of digits 2-9

    Returns:
        All possible letter combinations

    Example:
        letter_combinations("23") -> ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    """
    # TODO: Implement your solution here
    pass


def test_letter_combinations():
    # Test cases
    result1 = letter_combinations("23")
    expected1 = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sorted(result1) == sorted(expected1)

    assert letter_combinations("") == []
    assert letter_combinations("2") == ["a", "b", "c"]

    print("All test cases passed!")


if __name__ == "__main__":
    test_letter_combinations()
