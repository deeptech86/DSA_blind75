# #doubly_linked_list
# Delete All Occurrences of a Key in Doubly Linked List
# Source: Code & Debug - DSA Python Course Part 165

from typing import Optional

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def delete_all_occurrences(head: Optional[DLLNode], key: int) -> Optional[DLLNode]:
    """
    Delete all nodes with value equal to key from a doubly linked list.

    Args:
        head: Head of the doubly linked list
        key: Value to delete

    Returns:
        Head of the modified doubly linked list

    Example:
        [1, 2, 3, 2, 4, 2], key=2 -> [1, 3, 4]
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


def test_delete_all_occurrences():
    # Test cases
    head1 = list_to_dll([1, 2, 3, 2, 4, 2])
    assert dll_to_list(delete_all_occurrences(head1, 2)) == [1, 3, 4]

    head2 = list_to_dll([2, 2, 2])
    assert dll_to_list(delete_all_occurrences(head2, 2)) == []

    head3 = list_to_dll([1, 2, 3])
    assert dll_to_list(delete_all_occurrences(head3, 4)) == [1, 2, 3]

    head4 = list_to_dll([1])
    assert dll_to_list(delete_all_occurrences(head4, 1)) == []

    print("All test cases passed!")


if __name__ == "__main__":
    test_delete_all_occurrences()
