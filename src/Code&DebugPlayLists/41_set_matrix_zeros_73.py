# #matrix #array
# LeetCode 73: Set Matrix Zeros
# Source: Code & Debug - DSA Python Course Part 41

from typing import List

def set_zeroes(matrix: List[List[int]]) -> None:
    """
    If an element is 0, set its entire row and column to 0's.
    Must be done in-place.

    Args:
        matrix: An m x n integer matrix (modified in-place)

    Example:
        matrix = [[1,1,1],[1,0,1],[1,1,1]]
        set_zeroes(matrix)  # matrix becomes [[1,0,1],[0,0,0],[1,0,1]]
    """
    # TODO: Implement your solution here
    pass


def test_set_zeroes():
    # Test cases
    matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(matrix1)
    assert matrix1 == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeroes(matrix2)
    assert matrix2 == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

    matrix3 = [[1, 2, 3], [4, 5, 6]]
    set_zeroes(matrix3)
    assert matrix3 == [[1, 2, 3], [4, 5, 6]]

    print("All test cases passed!")


if __name__ == "__main__":
    test_set_zeroes()
