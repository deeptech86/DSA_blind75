# #backtracking #recursion
# Rat in a Maze - GFG Problem
# Source: Code & Debug - DSA Python Course Part 81

from typing import List

def find_paths(maze: List[List[int]]) -> List[str]:
    """
    Find all paths from top-left to bottom-right in a maze.
    1 = open cell, 0 = blocked cell
    Can move: Down (D), Left (L), Right (R), Up (U)

    Args:
        maze: N x N matrix with 0s and 1s

    Returns:
        All possible paths in lexicographical order

    Example:
        maze = [[1, 0, 0, 0],
                [1, 1, 0, 1],
                [1, 1, 0, 0],
                [0, 1, 1, 1]]
        find_paths(maze) -> ["DDRDRR", "DRDDRR"]
    """
    # TODO: Implement your solution here
    pass


def test_find_paths():
    # Test cases
    maze1 = [[1, 0, 0, 0],
             [1, 1, 0, 1],
             [1, 1, 0, 0],
             [0, 1, 1, 1]]
    assert sorted(find_paths(maze1)) == sorted(["DDRDRR", "DRDDRR"])

    maze2 = [[1, 0],
             [1, 1]]
    assert find_paths(maze2) == ["DR"]

    maze3 = [[0, 1],
             [1, 1]]
    assert find_paths(maze3) == []  # Starting cell is blocked

    print("All test cases passed!")


if __name__ == "__main__":
    test_find_paths()
