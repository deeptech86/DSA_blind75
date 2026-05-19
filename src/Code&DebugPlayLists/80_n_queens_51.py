# #backtracking #recursion
# LeetCode 51: N-Queens Problem
# Source: Code & Debug - DSA Python Course Part 80

from typing import List

def solve_n_queens(n: int) -> List[List[str]]:
    """
    Place n queens on an n x n chessboard such that no two queens attack each other.

    Args:
        n: Size of the chessboard and number of queens

    Returns:
        All distinct solutions where 'Q' represents a queen and '.' represents empty

    Example:
        solve_n_queens(4) -> [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    """
    # TODO: Implement your solution here
    pass


def test_solve_n_queens():
    # Test cases
    result1 = solve_n_queens(4)
    assert len(result1) == 2

    result2 = solve_n_queens(1)
    assert result2 == [["Q"]]

    result3 = solve_n_queens(2)
    assert result3 == []

    result4 = solve_n_queens(3)
    assert result4 == []

    print("All test cases passed!")


if __name__ == "__main__":
    test_solve_n_queens()
