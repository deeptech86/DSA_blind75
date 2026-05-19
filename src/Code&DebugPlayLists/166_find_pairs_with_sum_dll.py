# #doubly_linked_list #two_pointers
# Find Pairs with Given Sum in Doubly Linked List
# Source: Code & Debug - DSA Python Course Part 166

from typing import Optional, List, Tuple

class DLLNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


def find_pairs_with_sum(head: Optional[DLLNode], target: int) -> List[Tuple[int, int]]:
    """
    Find all pairs in a sorted doubly linked list with sum equal to target.

    Args:
        head: Head of a sorted doubly linked list
        target: The target sum

    Returns:
        List of pairs (tuples) that sum to target

    Example:
        [1, 2, 4, 5, 6, 8, 9], target=7 -> [(1, 6), (2, 5)]
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


def test_find_pairs_with_sum():
    # Test cases
    head1 = list_to_dll([1, 2, 4, 5, 6, 8, 9])
    assert find_pairs_with_sum(head1, 7) == [(1, 6), (2, 5)]

    head2 = list_to_dll([1, 5, 6])
    assert find_pairs_with_sum(head2, 6) == [(1, 5)]

    head3 = list_to_dll([1, 2, 3])
    assert find_pairs_with_sum(head3, 10) == []

    head4 = list_to_dll([1, 2, 3, 4])
    assert find_pairs_with_sum(head4, 5) == [(1, 4), (2, 3)]

    print("All test cases passed!")


if __name__ == "__main__":
    test_find_pairs_with_sum()
