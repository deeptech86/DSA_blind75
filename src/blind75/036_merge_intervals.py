"""
Problem: Merge Intervals
Technique: Line Sweep, Sorting
"""

def merge_intervals(intervals):
    """
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
    and return an array of the non-overlapping intervals that cover all the intervals in the input.
    
    Args:
        intervals: List[List[int]] - Array of intervals
        
    Returns:
        List[List[int]] - Merged intervals
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# Output: [[1, 6], [8, 10], [15, 18]]
# Explanation: Intervals [1, 3] and [2, 6] are merged into [1, 6]

# Example 2
# Input: intervals = [[1, 4], [4, 5]]
# Output: [[1, 5]]
# Explanation: Intervals [1, 4] and [4, 5] are merged into [1, 5]
