"""
LeetCode 141: Linked List Cycle
Difficulty: Easy
Pattern: Fast and Slow Pointers

Given head, the head of a linked list, determine if the linked list has a cycle in it.

Example:
Input: head = [3,2,0,-4], pos = 1
Output: true (There is a cycle in the linked list, where the tail connects to the 1st node)

Constraints:
- The number of the nodes in the list is in the range [0, 10^4].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using fast and slow pointers (Floyd's Cycle Detection)
    Hint: Use two pointers moving at different speeds, if they meet there's a cycle
    """
    pass

# Helper function to create a linked list with cycle
def create_cycle_list(values, pos):
    """Helper function to create test cases"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    nodes = [head]
    
    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        nodes.append(current)
    
    if pos != -1:
        current.next = nodes[pos]  # Create cycle
    
    return head

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 2, 0, -4], 1),  # Has cycle
        ([1, 2], 0),         # Has cycle
        ([1], -1),           # No cycle
        ([], -1)             # Empty list
    ]
    
    for values, pos in test_cases:
        head = create_cycle_list(values, pos)
        result = hasCycle(head)
        print(f"Values: {values}, pos: {pos}")
        print(f"Has cycle: {result}\n")
