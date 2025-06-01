"""
Problem: Meeting Rooms
Technique: Line Sweep, Sorting
"""

def meeting_rooms(intervals):
    """
    Given an array of meeting time intervals where intervals[i] = [starti, endi],
    determine if a person could attend all meetings.
    
    Args:
        intervals: List[List[int]] - Array of meeting time intervals
        
    Returns:
        bool - True if a person can attend all meetings, False otherwise
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: intervals = [[0, 30], [5, 10], [15, 20]]
# Output: False
# Explanation: Cannot attend all meetings because [0, 30] overlaps with [5, 10] and [15, 20]

# Example 2
# Input: intervals = [[7, 10], [2, 4]]
# Output: True
# Explanation: Can attend all meetings, as they don't overlap
