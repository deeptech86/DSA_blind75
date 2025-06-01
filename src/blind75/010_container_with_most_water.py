"""
Problem: Container with Most Water
Technique: Two Pointers (Opposite Direction)
"""

def container_with_most_water(height):
    """
    Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai),
    n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
    Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
    
    Args:
        height: List[int] - Array of heights
        
    Returns:
        int - Maximum amount of water a container can store
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49
# Explanation: The container formed by lines at index 1 and 8 with heights 8 and 7 contains 49 units of water

# Example 2
# Input: height = [1, 1]
# Output: 1
# Explanation: The container formed by lines at index 0 and 1 with heights 1 and 1 contains 1 unit of water
