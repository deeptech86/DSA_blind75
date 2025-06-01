"""
Problem: Course Schedule
Technique: Directed Graph / Topological Sort
"""

def course_schedule(numCourses, prerequisites):
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
    You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that
    you must take course bi first if you want to take course ai.
    Return true if you can finish all courses. Otherwise, return false.
    
    Args:
        numCourses: int - Number of courses
        prerequisites: List[List[int]] - Array of prerequisite pairs
        
    Returns:
        bool - True if all courses can be finished, False otherwise
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: True
# Explanation: There are 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

# Example 2
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: False
# Explanation: There are 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
