# #stack #design
# LeetCode 155: Min Stack - Get Minimum in O(1)
# Source: Code & Debug - DSA Python Course Part 89

class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving
    the minimum element in constant time.

    Operations:
    - push(val): Push element onto stack
    - pop(): Remove the top element
    - top(): Get the top element
    - getMin(): Retrieve the minimum element in the stack
    """

    def __init__(self):
        """Initialize your data structure here."""
        # TODO: Implement initialization
        pass

    def push(self, val: int) -> None:
        """Push element val onto stack."""
        # TODO: Implement push
        pass

    def pop(self) -> None:
        """Remove the top element."""
        # TODO: Implement pop
        pass

    def top(self) -> int:
        """Get the top element."""
        # TODO: Implement top
        pass

    def getMin(self) -> int:
        """Retrieve the minimum element in the stack."""
        # TODO: Implement getMin
        pass


def test_min_stack():
    # Test cases
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2

    # Additional test
    minStack2 = MinStack()
    minStack2.push(1)
    minStack2.push(2)
    assert minStack2.getMin() == 1
    minStack2.push(-1)
    assert minStack2.getMin() == -1
    minStack2.pop()
    assert minStack2.getMin() == 1

    print("All test cases passed!")


if __name__ == "__main__":
    test_min_stack()
