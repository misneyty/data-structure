from collections import deque


class Queue:
    """A first-in, first-out (FIFO) data structure."""

    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self._data.append(item)

    def dequeue(self):
        """Remove and return the front item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()

    def front(self):
        """Return the front item without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("front of empty queue")
        return self._data[0]

    def is_empty(self):
        """Return True if the queue has no items."""
        return len(self._data) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self._data)

    def __repr__(self):
        return f"Queue({list(self._data)})"
