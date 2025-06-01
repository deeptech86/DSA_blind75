"""
Problem: Find Median from Data Stream
Technique: Data Structure Design, Priority Queue (Two Heaps)
"""

import heapq

class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # TODO: Implement initialization
        pass
        
    def addNum(self, num):
        """
        Adds a number into the data structure.
        
        Args:
            num: int - Number to add
            
        Returns:
            None
        """
        # TODO: Implement addNum
        pass
        
    def findMedian(self):
        """
        Returns the median of all elements so far.
        
        Returns:
            float - Median of all elements
        """
        # TODO: Implement findMedian
        pass


# Example 1
# Input:
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output:
# [null, null, null, 1.5, null, 2.0]
# Explanation:
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr = [1, 2, 3]
# medianFinder.findMedian(); // return 2.0

# Example 2
# Input: 
# ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [2], [], [1], []]
# Output:
# [null, null, 2.0, null, 1.5]
# Explanation:
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(2);    // arr = [2]
# medianFinder.findMedian(); // return 2.0
# medianFinder.addNum(1);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5
