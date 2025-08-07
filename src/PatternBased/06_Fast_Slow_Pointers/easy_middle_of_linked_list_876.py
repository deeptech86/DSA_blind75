"""
LeetCode 876: Middle of the Linked List
Difficulty: Easy
Pattern: Fast and Slow Pointers

Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example:
Input: head = [1,2,3,4,5]
Output: [3,4,5] (The middle node of the list is node 3)

Constraints:
- The number of nodes in the list is in the range [1, 100].
- 1 <= Node.val <= 100
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using fast and slow pointers
    Hint: Move slow pointer one step, fast pointer two steps. When fast reaches end, slow is at middle.
    """
    pass

# Helper functions
def create_linked_list(values):
    """Helper function to create test cases"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """Helper function to convert linked list to list for output"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
        [1],
        [1, 2]
    ]
    
    for values in test_cases:
        head = create_linked_list(values)
        middle = middleNode(head)
        result = linked_list_to_list(middle)
        print(f"Input: {values}")
        print(f"Middle to end: {result}\n")
