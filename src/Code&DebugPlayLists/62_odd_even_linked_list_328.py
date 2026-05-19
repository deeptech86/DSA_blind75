# #linked_list
# LeetCode 328: Odd Even Linked List - Rearrange Nodes
# Source: Code & Debug - DSA Python Course Part 62

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Group all odd-indexed nodes together followed by even-indexed nodes.
    The first node is considered odd (index 1).

    Args:
        head: Head of the linked list

    Returns:
        Head of the rearranged linked list

    Example:
        [1, 2, 3, 4, 5] -> [1, 3, 5, 2, 4]
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


def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test_odd_even_list():
    # Test cases
    head1 = list_to_linked_list([1, 2, 3, 4, 5])
    assert linked_list_to_list(odd_even_list(head1)) == [1, 3, 5, 2, 4]

    head2 = list_to_linked_list([2, 1, 3, 5, 6, 4, 7])
    assert linked_list_to_list(odd_even_list(head2)) == [2, 3, 6, 7, 1, 5, 4]

    head3 = list_to_linked_list([1, 2])
    assert linked_list_to_list(odd_even_list(head3)) == [1, 2]

    head4 = list_to_linked_list([1])
    assert linked_list_to_list(odd_even_list(head4)) == [1]

    print("All test cases passed!")


if __name__ == "__main__":
    test_odd_even_list()
