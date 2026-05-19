# #linked_list #two_pointers
# LeetCode 141: Linked List Cycle (Floyd's Cycle Detection)
# Source: Code & Debug - DSA Python Course Part 59

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect if a linked list has a cycle using Floyd's algorithm.

    Args:
        head: Head of the linked list

    Returns:
        True if cycle exists, False otherwise

    Example:
        [3, 2, 0, -4] with tail connecting to index 1 -> True
    """
    # TODO: Implement your solution here
    pass


def test_has_cycle():
    # Test case 1: Cycle exists
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Cycle
    assert has_cycle(node1) == True

    # Test case 2: No cycle
    head2 = ListNode(1)
    head2.next = ListNode(2)
    assert has_cycle(head2) == False

    # Test case 3: Single node, no cycle
    head3 = ListNode(1)
    assert has_cycle(head3) == False

    # Test case 4: Empty list
    assert has_cycle(None) == False

    print("All test cases passed!")


if __name__ == "__main__":
    test_has_cycle()
