# #stack #queue
# LeetCode 232: Implement Queue using Stacks
# Source: Code & Debug - DSA Python Course Part 86

class MyQueue:
    """
    Implement a FIFO queue using only two stacks.

    Operations:
    - push(x): Push element x to back of queue
    - pop(): Remove and return front element
    - peek(): Get the front element
    - empty(): Return whether queue is empty
    """

    def __init__(self):
        """Initialize your data structure here."""
        # TODO: Implement initialization
        pass

    def push(self, x: int) -> None:
        """Push element x to the back of queue."""
        # TODO: Implement push
        pass

    def pop(self) -> int:
        """Remove and return the front element."""
        # TODO: Implement pop
        pass

    def peek(self) -> int:
        """Get the front element."""
        # TODO: Implement peek
        pass

    def empty(self) -> bool:
        """Return whether the queue is empty."""
        # TODO: Implement empty
        pass


def test_my_queue():
    # Test cases
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    assert queue.peek() == 1
    assert queue.pop() == 1
    assert queue.empty() == False
    assert queue.pop() == 2
    assert queue.empty() == True

    print("All test cases passed!")


if __name__ == "__main__":
    test_my_queue()
