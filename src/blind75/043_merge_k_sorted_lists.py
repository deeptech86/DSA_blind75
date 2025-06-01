"""
Problem: Merge K Sorted Lists
Technique: Priority Queue, Divide and Conquer
"""

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_sorted_lists(lists):
    """
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
    Merge all the linked-lists into one sorted linked-list and return it.
    
    Args:
        lists: List[ListNode] - Array of heads of k sorted linked lists
        
    Returns:
        ListNode - Head of the merged, sorted linked list
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# Output: [1, 1, 2, 3, 4, 4, 5, 6]
# Explanation: Merging all k sorted lists into one sorted list

# Example 2
# Input: lists = []
# Output: []
# Explanation: When there are no lists, return an empty list
