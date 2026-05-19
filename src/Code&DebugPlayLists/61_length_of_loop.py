# #linked_list #two_pointers
# Find Length of Loop in Linked List (Floyd Cycle Detection)
# Source: Code & Debug - DSA Python Course Part 61

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_loop_length(head: Optional[ListNode]) -> int:
    """
    Find the length of the loop in a linked list.

    Args:
        head: Head of the linked list

    Returns:
        Length of the loop, or 0 if no loop exists

    Example:
        [1, 2, 3, 4, 5] with 5 connecting to 2 -> 4 (loop: 2->3->4->5->2)
    """
    # TODO: Implement your solution here
    pass


def test_find_loop_length():
    # Test case 1: Loop of length 4
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2  # Loop: 2->3->4->5->2, length 4
    assert find_loop_length(node1) == 4

    # Test case 2: No loop
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)
    assert find_loop_length(head2) == 0

    # Test case 3: Single node loop
    head3 = ListNode(1)
    head3.next = head3
    assert find_loop_length(head3) == 1

    print("All test cases passed!")


if __name__ == "__main__":
    test_find_loop_length()
