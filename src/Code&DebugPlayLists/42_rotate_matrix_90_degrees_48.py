# #matrix #array
# LeetCode 48: Rotate Matrix by 90 Degrees (Clockwise)
# Source: Code & Debug - DSA Python Course Part 42

from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Rotate the matrix by 90 degrees clockwise in-place.

    Args:
        matrix: An n x n 2D matrix (modified in-place)

    Example:
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        rotate(matrix)  # matrix becomes [[7,4,1],[8,5,2],[9,6,3]]
    """
    # TODO: Implement your solution here
    pass


def test_rotate():
    # Test cases
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix1)
    assert matrix1 == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(matrix2)
    assert matrix2 == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

    matrix3 = [[1]]
    rotate(matrix3)
    assert matrix3 == [[1]]

    print("All test cases passed!")


if __name__ == "__main__":
    test_rotate()
