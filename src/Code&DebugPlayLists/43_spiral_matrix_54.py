# #matrix #array
# LeetCode 54: Print the Matrix in Spiral Order
# Source: Code & Debug - DSA Python Course Part 43

from typing import List

def spiral_order(matrix: List[List[int]]) -> List[int]:
    """
    Return all elements of the matrix in spiral order.

    Args:
        matrix: An m x n matrix

    Returns:
        Elements in spiral order

    Example:
        spiral_order([[1,2,3],[4,5,6],[7,8,9]]) -> [1,2,3,6,9,8,7,4,5]
    """
    # TODO: Implement your solution here
    pass


def test_spiral_order():
    # Test cases
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert spiral_order([[1]]) == [1]
    assert spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]
    print("All test cases passed!")


if __name__ == "__main__":
    test_spiral_order()
