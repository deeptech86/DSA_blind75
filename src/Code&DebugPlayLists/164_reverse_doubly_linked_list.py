# #doubly_linked_list
# Reverse a Doubly Linked List
# Source: Code & Debug - DSA Python Course Part 164

from typing import Optional

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def reverse_dll(head: Optional[DLLNode]) -> Optional[DLLNode]:
    """
    Reverse a doubly linked list.

    Args:
        head: Head of the doubly linked list

    Returns:
        Head of the reversed doubly linked list

    Example:
        [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]
    """
    # TODO: Implement your solution here
    pass


def list_to_dll(arr):
    if not arr:
        return None
    head = DLLNode(arr[0])
    current = head
    for val in arr[1:]:
        new_node = DLLNode(val, prev=current)
        current.next = new_node
        current = new_node
    return head


def dll_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def test_reverse_dll():
    # Test cases
    head1 = list_to_dll([1, 2, 3, 4, 5])
    assert dll_to_list(reverse_dll(head1)) == [5, 4, 3, 2, 1]

    head2 = list_to_dll([1, 2])
    assert dll_to_list(reverse_dll(head2)) == [2, 1]

    head3 = list_to_dll([1])
    assert dll_to_list(reverse_dll(head3)) == [1]

    head4 = list_to_dll([])
    assert dll_to_list(reverse_dll(head4)) == []

    print("All test cases passed!")


if __name__ == "__main__":
    test_reverse_dll()
