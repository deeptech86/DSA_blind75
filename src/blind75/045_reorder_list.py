"""
Problem: Reorder List
Technique: Two Pointers (Same Direction)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorder_list(head):
    """
    Given a singly linked list L: L0→L1→…→Ln-1→Ln,
    reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
    
    Args:
        head: ListNode - Head of the linked list
        
    Returns:
        None - Modify the list in-place
    """
    # TODO: Implement solution
    pass


# Example 1
# Input: head = [1, 2, 3, 4]
# Output: [1, 4, 2, 3]
# Explanation: Reordering to 1→4→2→3

# Example 2
# Input: head = [1, 2, 3, 4, 5]
# Output: [1, 5, 2, 4, 3]
# Explanation: Reordering to 1→5→2→4→3
