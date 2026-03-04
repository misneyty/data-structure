import pytest

from stack import Stack
from queue import Queue
from linked_list import LinkedList
from binary_search_tree import BinarySearchTree


# ---------------------------------------------------------------------------
# Stack tests
# ---------------------------------------------------------------------------

class TestStack:
    def test_push_and_peek(self):
        s = Stack()
        s.push(1)
        assert s.peek() == 1

    def test_push_multiple_and_peek_returns_top(self):
        s = Stack()
        s.push(1)
        s.push(2)
        assert s.peek() == 2

    def test_pop_returns_top(self):
        s = Stack()
        s.push(10)
        s.push(20)
        assert s.pop() == 20
        assert s.pop() == 10

    def test_pop_empty_raises(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.pop()

    def test_peek_empty_raises(self):
        s = Stack()
        with pytest.raises(IndexError):
            s.peek()

    def test_is_empty(self):
        s = Stack()
        assert s.is_empty()
        s.push(1)
        assert not s.is_empty()

    def test_size(self):
        s = Stack()
        assert s.size() == 0
        s.push(1)
        s.push(2)
        assert s.size() == 2
        s.pop()
        assert s.size() == 1


# ---------------------------------------------------------------------------
# Queue tests
# ---------------------------------------------------------------------------

class TestQueue:
    def test_enqueue_and_front(self):
        q = Queue()
        q.enqueue(1)
        assert q.front() == 1

    def test_fifo_order(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        assert q.dequeue() == 1
        assert q.dequeue() == 2
        assert q.dequeue() == 3

    def test_dequeue_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.dequeue()

    def test_front_empty_raises(self):
        q = Queue()
        with pytest.raises(IndexError):
            q.front()

    def test_is_empty(self):
        q = Queue()
        assert q.is_empty()
        q.enqueue(5)
        assert not q.is_empty()

    def test_size(self):
        q = Queue()
        assert q.size() == 0
        q.enqueue(1)
        q.enqueue(2)
        assert q.size() == 2
        q.dequeue()
        assert q.size() == 1


# ---------------------------------------------------------------------------
# LinkedList tests
# ---------------------------------------------------------------------------

class TestLinkedList:
    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.to_list() == [1, 2, 3]

    def test_prepend(self):
        ll = LinkedList()
        ll.append(2)
        ll.prepend(1)
        assert ll.to_list() == [1, 2]

    def test_delete_middle(self):
        ll = LinkedList()
        for v in [1, 2, 3]:
            ll.append(v)
        ll.delete(2)
        assert ll.to_list() == [1, 3]

    def test_delete_head(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.delete(1)
        assert ll.to_list() == [2]

    def test_delete_not_found_raises(self):
        ll = LinkedList()
        ll.append(1)
        with pytest.raises(ValueError):
            ll.delete(99)

    def test_search_found(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        assert ll.search(2)

    def test_search_not_found(self):
        ll = LinkedList()
        ll.append(1)
        assert not ll.search(99)

    def test_size(self):
        ll = LinkedList()
        assert ll.size() == 0
        ll.append(1)
        ll.append(2)
        assert ll.size() == 2

    def test_is_empty(self):
        ll = LinkedList()
        assert ll.is_empty()
        ll.append(1)
        assert not ll.is_empty()


# ---------------------------------------------------------------------------
# BinarySearchTree tests
# ---------------------------------------------------------------------------

class TestBinarySearchTree:
    def test_insert_and_inorder(self):
        bst = BinarySearchTree()
        for v in [5, 3, 7, 1, 4]:
            bst.insert(v)
        assert bst.inorder() == [1, 3, 4, 5, 7]

    def test_search_found(self):
        bst = BinarySearchTree()
        bst.insert(10)
        bst.insert(5)
        assert bst.search(5)

    def test_search_not_found(self):
        bst = BinarySearchTree()
        bst.insert(10)
        assert not bst.search(99)

    def test_delete_leaf(self):
        bst = BinarySearchTree()
        for v in [5, 3, 7]:
            bst.insert(v)
        bst.delete(3)
        assert bst.inorder() == [5, 7]

    def test_delete_node_with_two_children(self):
        bst = BinarySearchTree()
        for v in [5, 3, 7, 1, 4]:
            bst.insert(v)
        bst.delete(3)
        assert bst.inorder() == [1, 4, 5, 7]

    def test_delete_not_found_raises(self):
        bst = BinarySearchTree()
        bst.insert(5)
        with pytest.raises(ValueError):
            bst.delete(99)

    def test_height_empty(self):
        bst = BinarySearchTree()
        assert bst.height() == 0

    def test_height(self):
        bst = BinarySearchTree()
        for v in [5, 3, 7]:
            bst.insert(v)
        assert bst.height() == 2

    def test_duplicate_insert_ignored(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(5)
        assert bst.inorder() == [5]
