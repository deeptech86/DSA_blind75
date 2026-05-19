# #stack #data_structure
# Implement Stack using Arrays
# Source: Code & Debug - DSA Python Course Part 82

class Stack:
    """
    Implement a stack using a list (array).

    Operations:
    - push(x): Add element x to top of stack
    - pop(): Remove and return top element
    - peek/top(): Return top element without removing
    - is_empty(): Check if stack is empty
    - size(): Return number of elements
    """

    def __init__(self, capacity: int = 1000):
        """Initialize stack with optional capacity."""
        # TODO: Implement initialization
        pass

    def push(self, x: int) -> None:
        """Push element onto stack."""
        # TODO: Implement push
        pass

    def pop(self) -> int:
        """Remove and return top element. Return -1 if empty."""
        # TODO: Implement pop
        pass

    def top(self) -> int:
        """Return top element without removing. Return -1 if empty."""
        # TODO: Implement top/peek
        pass

    def is_empty(self) -> bool:
        """Return True if stack is empty."""
        # TODO: Implement is_empty
        pass

    def size(self) -> int:
        """Return number of elements in stack."""
        # TODO: Implement size
        pass


def test_stack():
    # Test cases
    stack = Stack()
    assert stack.is_empty() == True
    assert stack.size() == 0

    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.size() == 3
    assert stack.top() == 3
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.top() == 1
    assert stack.is_empty() == False
    assert stack.pop() == 1
    assert stack.is_empty() == True
    assert stack.pop() == -1

    print("All test cases passed!")


if __name__ == "__main__":
    test_stack()
