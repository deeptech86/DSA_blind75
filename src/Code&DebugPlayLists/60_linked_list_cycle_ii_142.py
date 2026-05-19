# #linked_list #two_pointers
# LeetCode 142: Linked List Cycle II - Find the Cycle Starting Point
# Source: Code & Debug - DSA Python Course Part 60

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the node where the cycle begins in a linked list.

    Args:
        head: Head of the linked list

    Returns:
        The node where cycle begins, or None if no cycle

    Example:
        [3, 2, 0, -4] with tail connecting to index 1 -> node with value 2
    """
    # TODO: Implement your solution here
    pass


def test_detect_cycle():
    # Test case 1: Cycle exists at node 2
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Cycle starts at node2
    assert detect_cycle(node1) == node2

    # Test case 2: No cycle
    head2 = ListNode(1)
    head2.next = ListNode(2)
    assert detect_cycle(head2) == None

    # Test case 3: Single node with cycle to itself
    head3 = ListNode(1)
    head3.next = head3
    assert detect_cycle(head3) == head3

    # Test case 4: Empty list
    assert detect_cycle(None) == None

    print("All test cases passed!")


if __name__ == "__main__":
    test_detect_cycle()
