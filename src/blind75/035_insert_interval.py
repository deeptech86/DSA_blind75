"""
Problem: Insert Interval
Technique: Line Sweep
"""

def insert_interval(intervals, newInterval):
    """
    Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
    You may assume that the intervals were initially sorted according to their start times.
    
    Args:
        intervals: List[List[int]] - Array of intervals where intervals[i] = [starti, endi]
        newInterval: List[int] - New interval to insert
        
    Returns:
        List[List[int]] - Updated intervals
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
# Output: [[1, 5], [6, 9]]
# Explanation: Intervals [1, 3] and [2, 5] are merged into [1, 5]

# Example 2
# Input: intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval = [4, 8]
# Output: [[1, 2], [3, 10], [12, 16]]
# Explanation: Intervals [3, 5], [6, 7], [8, 10] are merged with [4, 8] into [3, 10]
