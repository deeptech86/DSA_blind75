# #stack #queue
# LeetCode 225: Implement Stack using Queues
# Source: Code & Debug - DSA Python Course Part 85

from collections import deque

class MyStack:
    """
    Implement a LIFO stack using only two queues.

    Operations:
    - push(x): Push element x onto stack
    - pop(): Remove and return top element
    - top(): Get the top element
    - empty(): Return whether stack is empty
    """

    def __init__(self):
        """Initialize your data structure here."""
        # TODO: Implement initialization
        pass

    def push(self, x: int) -> None:
        """Push element x onto stack."""
        # TODO: Implement push
        pass

    def pop(self) -> int:
        """Remove and return the top element."""
        # TODO: Implement pop
        pass

    def top(self) -> int:
        """Get the top element."""
        # TODO: Implement top
        pass

    def empty(self) -> bool:
        """Return whether the stack is empty."""
        # TODO: Implement empty
        pass


def test_my_stack():
    # Test cases
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    assert stack.top() == 2
    assert stack.pop() == 2
    assert stack.empty() == False
    assert stack.pop() == 1
    assert stack.empty() == True

    print("All test cases passed!")


if __name__ == "__main__":
    test_my_stack()
