class Stack:
    """A last-in, first-out (LIFO) data structure."""

    def __init__(self):
        self._data = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self._data.append(item)

    def pop(self):
        """Remove and return the top item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        """Return the top item without removing it. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        """Return True if the stack has no items."""
        return len(self._data) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"
