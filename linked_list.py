class Node:
    """A single node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list."""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node with the given data at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """Add a node with the given data at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Remove the first node with the given data. Raises ValueError if not found."""
        if self.head is None:
            raise ValueError(f"{data} not found in list")
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError(f"{data} not found in list")

    def search(self, data):
        """Return True if a node with the given data exists."""
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    def to_list(self):
        """Return a Python list of all node values."""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def size(self):
        """Return the number of nodes in the list."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        """Return True if the list has no nodes."""
        return self.head is None

    def __repr__(self):
        return " -> ".join(str(v) for v in self.to_list())
