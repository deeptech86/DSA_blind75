"""
LeetCode 142: Linked List Cycle II
Difficulty: Medium
Pattern: Fast and Slow Pointers

Given the head of a linked list, return the node where the cycle begins. 
If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be 
reached again by continuously following the next pointer.

Example:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1

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

def detectCycle(head):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    TODO: Implement the solution using Floyd's cycle detection algorithm
    Hint: First detect cycle, then find the start of the cycle using two pointers
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
        return head, nodes[pos]
    
    return head, None

# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 2, 0, -4], 1),  # Cycle starts at index 1
        ([1, 2], 0),         # Cycle starts at index 0
        ([1], -1),           # No cycle
        ([], -1)             # Empty list
    ]
    
    for values, pos in test_cases:
        if values:
            head, expected_cycle_start = create_cycle_list(values, pos)
            result = detectCycle(head)
            
            if result and expected_cycle_start:
                cycle_start_val = result.val
            else:
                cycle_start_val = None
            
            print(f"Values: {values}, pos: {pos}")
            print(f"Cycle start value: {cycle_start_val}\n")
        else:
            print("Empty list: No cycle\n")
