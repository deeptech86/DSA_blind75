# #queue #data_structure
# Implement Queue using Arrays
# Source: Code & Debug - DSA Python Course Part 83

class Queue:
    """
    Implement a queue using a list (array).

    Operations:
    - enqueue(x): Add element x to back of queue
    - dequeue(): Remove and return front element
    - front(): Return front element without removing
    - is_empty(): Check if queue is empty
    - size(): Return number of elements
    """

    def __init__(self, capacity: int = 1000):
        """Initialize queue with optional capacity."""
        # TODO: Implement initialization
        pass

    def enqueue(self, x: int) -> None:
        """Add element to back of queue."""
        # TODO: Implement enqueue
        pass

    def dequeue(self) -> int:
        """Remove and return front element. Return -1 if empty."""
        # TODO: Implement dequeue
        pass

    def front(self) -> int:
        """Return front element without removing. Return -1 if empty."""
        # TODO: Implement front
        pass

    def is_empty(self) -> bool:
        """Return True if queue is empty."""
        # TODO: Implement is_empty
        pass

    def size(self) -> int:
        """Return number of elements in queue."""
        # TODO: Implement size
        pass


def test_queue():
    # Test cases
    queue = Queue()
    assert queue.is_empty() == True
    assert queue.size() == 0

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.size() == 3
    assert queue.front() == 1
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.front() == 3
    assert queue.is_empty() == False
    assert queue.dequeue() == 3
    assert queue.is_empty() == True
    assert queue.dequeue() == -1

    print("All test cases passed!")


if __name__ == "__main__":
    test_queue()
