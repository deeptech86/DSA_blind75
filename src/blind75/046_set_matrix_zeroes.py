"""
Problem: Set Matrix Zeroes
Technique: Matrix Traversal
"""

def set_matrix_zeroes(matrix):
    """
    Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.
    
    Args:
        matrix: List[List[int]] - Input matrix
        
    Returns:
        None - Modify the matrix in-place
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: matrix = [
#   [1, 1, 1],
#   [1, 0, 1],
#   [1, 1, 1]
# ]
# Output: [
#   [1, 0, 1],
#   [0, 0, 0],
#   [1, 0, 1]
# ]
# Explanation: The zero in the middle causes its entire row and column to be set to zero

# Example 2
# Input: matrix = [
#   [0, 1, 2, 0],
#   [3, 4, 5, 2],
#   [1, 3, 1, 5]
# ]
# Output: [
#   [0, 0, 0, 0],
#   [0, 4, 5, 0],
#   [0, 3, 1, 0]
# ]
# Explanation: The zeros in the first row and last column cause those rows and columns to be set to zero
