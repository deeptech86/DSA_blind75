# #doubly_linked_list
# Remove Duplicates from a Sorted Doubly Linked List
# Source: Code & Debug - DSA Python Course Part 167

from typing import Optional

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def remove_duplicates(head: Optional[DLLNode]) -> Optional[DLLNode]:
    """
    Remove duplicate nodes from a sorted doubly linked list.

    Args:
        head: Head of a sorted doubly linked list

    Returns:
        Head of the list with duplicates removed

    Example:
        [1, 1, 2, 3, 3, 4, 4, 4, 5] -> [1, 2, 3, 4, 5]
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


def test_remove_duplicates():
    # Test cases
    head1 = list_to_dll([1, 1, 2, 3, 3, 4, 4, 4, 5])
    assert dll_to_list(remove_duplicates(head1)) == [1, 2, 3, 4, 5]

    head2 = list_to_dll([1, 1, 1, 1])
    assert dll_to_list(remove_duplicates(head2)) == [1]

    head3 = list_to_dll([1, 2, 3])
    assert dll_to_list(remove_duplicates(head3)) == [1, 2, 3]

    head4 = list_to_dll([])
    assert dll_to_list(remove_duplicates(head4)) == []

    print("All test cases passed!")


if __name__ == "__main__":
    test_remove_duplicates()
