#circular linked List

def fast_slow_template(head):
    """
    General template for fast & slow pointers
    """
    if not head:
        return None

    slow = head
    fast = head

    # Customize the movement pattern based on problem:
    # - Cycle detection: fast moves 2, slow moves 1
    # - Find middle: same as cycle detection
    # - Find kth from end: fast moves k steps ahead first

    while fast and fast.next:  # Adjust condition as needed
        slow = slow.next  # Slow pointer moves 1 step
        fast = fast.next.next  # Fast pointer moves 2 steps

        # Add problem-specific logic here
        # if slow == fast:  # For cycle detection
        #     return True

    return slow