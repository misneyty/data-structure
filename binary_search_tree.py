class BSTNode:
    """A node in a binary search tree."""

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    """A binary search tree (BST)."""

    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert a key into the BST."""
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert(node.right, key)
        # duplicate keys are ignored

    def search(self, key):
        """Return True if the key exists in the BST."""
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        """Remove the node with the given key from the BST."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            raise ValueError(f"{key} not found in BST")
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node to delete found
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Node has two children: replace with in-order successor
            successor = self._min_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        return node

    def _min_node(self, node):
        """Return the node with the minimum key in the subtree."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        """Return a list of keys in ascending order."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def height(self):
        """Return the height of the BST (0 for empty tree)."""
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def __repr__(self):
        return f"BST(inorder={self.inorder()})"
