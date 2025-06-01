"""
Problem: Merge Two Sorted Lists
Technique: Two Pointers (Same Direction)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_sorted_lists(l1, l2):
    """
    Merge two sorted linked lists and return it as a sorted list.
    
    Args:
        l1: ListNode - Head of the first sorted linked list
        l2: ListNode - Head of the second sorted linked list
        
    Returns:
        ListNode - Head of the merged, sorted linked list
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: l1 = [1, 2, 4], l2 = [1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]
# Explanation: Merging the two sorted lists

# Example 2
# Input: l1 = [], l2 = [0]
# Output: [0]
# Explanation: When one list is empty, return the other list
