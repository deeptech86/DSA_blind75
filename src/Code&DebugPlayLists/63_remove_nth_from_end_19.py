# #linked_list #two_pointers
# LeetCode 19: Remove Nth Node from End of List
# Source: Code & Debug - DSA Python Course Part 63

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Remove the nth node from the end of the list.

    Args:
        head: Head of the linked list
        n: Position from end (1-indexed)

    Returns:
        Head of the modified linked list

    Example:
        [1, 2, 3, 4, 5], n=2 -> [1, 2, 3, 5]
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


def test_remove_nth_from_end():
    # Test cases
    head1 = list_to_linked_list([1, 2, 3, 4, 5])
    assert linked_list_to_list(remove_nth_from_end(head1, 2)) == [1, 2, 3, 5]

    head2 = list_to_linked_list([1])
    assert linked_list_to_list(remove_nth_from_end(head2, 1)) == []

    head3 = list_to_linked_list([1, 2])
    assert linked_list_to_list(remove_nth_from_end(head3, 1)) == [1]

    head4 = list_to_linked_list([1, 2])
    assert linked_list_to_list(remove_nth_from_end(head4, 2)) == [2]

    print("All test cases passed!")


if __name__ == "__main__":
    test_remove_nth_from_end()
