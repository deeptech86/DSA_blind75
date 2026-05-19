# #linked_list #two_pointers
# LeetCode 876: Middle of the Linked List (Tortoise-Hare Approach)
# Source: Code & Debug - DSA Python Course Part 57

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Find the middle node of a linked list.
    If two middle nodes, return the second middle node.

    Args:
        head: Head of the linked list

    Returns:
        The middle node

    Example:
        [1, 2, 3, 4, 5] -> node with value 3
        [1, 2, 3, 4, 5, 6] -> node with value 4
    """
    # TODO: Implement your solution here
    pass


def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def test_middle_node():
    # Test cases
    head1 = list_to_linked_list([1, 2, 3, 4, 5])
    assert middle_node(head1).val == 3

    head2 = list_to_linked_list([1, 2, 3, 4, 5, 6])
    assert middle_node(head2).val == 4

    head3 = list_to_linked_list([1])
    assert middle_node(head3).val == 1

    head4 = list_to_linked_list([1, 2])
    assert middle_node(head4).val == 2

    print("All test cases passed!")


if __name__ == "__main__":
    test_middle_node()
