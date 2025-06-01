"""
Problem: Detect Cycle in a Linked List
Technique: Two Pointers (Cycle Finding)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_cycle(head):
    """
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    
    Args:
        head: ListNode - Head of the linked list
        
    Returns:
        bool - True if there is a cycle in the linked list, False otherwise
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: head = [3, 2, 0, -4], pos = 1
# Output: True
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed)

# Example 2
# Input: head = [1, 2], pos = 0
# Output: True
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node
