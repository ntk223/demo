"""
Cấu trúc dữ liệu cơ bản (Basic Data Structures)
===============================================
Cài đặt thuần Python để minh họa nguyên lý hoạt động.
"""

from collections import deque


class Stack:
    """Ngăn xếp LIFO — push/pop/peek đều O(1)."""

    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop từ stack rỗng")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek từ stack rỗng")
        return self._items[-1]

    def is_empty(self):
        return not self._items

    def __len__(self):
        return len(self._items)


class MinStack(Stack):
    """Stack hỗ trợ truy vấn phần tử nhỏ nhất trong O(1)."""

    def __init__(self):
        super().__init__()
        self._mins = []

    def push(self, item):
        super().push(item)
        self._mins.append(item if not self._mins or item < self._mins[-1] else self._mins[-1])

    def pop(self):
        self._mins.pop()
        return super().pop()

    def min(self):
        if not self._mins:
            raise IndexError("min từ stack rỗng")
        return self._mins[-1]


class Queue:
    """Hàng đợi FIFO — enqueue/dequeue O(1) nhờ collections.deque."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue từ queue rỗng")
        return self._items.popleft()

    def peek(self):
        if not self._items:
            raise IndexError("peek từ queue rỗng")
        return self._items[0]

    def is_empty(self):
        return not self._items

    def __len__(self):
        return len(self._items)


class LinkedList:
    """Danh sách liên kết đơn: append, prepend, remove, contains."""

    class _Node:
        __slots__ = ("value", "next")

        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self._head = None
        self._size = 0

    def append(self, value):
        node = self._Node(value)
        if self._head is None:
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node
        self._size += 1

    def prepend(self, value):
        node = self._Node(value)
        node.next = self._head
        self._head = node
        self._size += 1

    def remove(self, value):
        """Xóa phần tử đầu tiên có giá trị bằng value. Trả về True nếu xóa được."""
        prev, cur = None, self._head
        while cur:
            if cur.value == value:
                if prev is None:
                    self._head = cur.next
                else:
                    prev.next = cur.next
                self._size -= 1
                return True
            prev, cur = cur, cur.next
        return False

    def contains(self, value):
        cur = self._head
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def __iter__(self):
        cur = self._head
        while cur:
            yield cur.value
            cur = cur.next

    def __len__(self):
        return self._size


class BinarySearchTree:
    """Cây tìm kiếm nhị phân (BST): insert, contains, duyệt in-order tăng dần."""

    class _Node:
        __slots__ = ("key", "left", "right")

        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    def __init__(self):
        self._root = None
        self._size = 0

    def insert(self, key):
        def _insert(node, key):
            if node is None:
                self._size += 1
                return BinarySearchTree._Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            return node  # key trùng: bỏ qua

        self._root = _insert(self._root, key)

    def contains(self, key):
        node = self._root
        while node:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def in_order(self):
        """Duyệt in-order — trả về danh sách các khóa theo thứ tự tăng dần."""
        out = []

        def walk(node):
            if node:
                walk(node.left)
                out.append(node.key)
                walk(node.right)

        walk(self._root)
        return out

    def __len__(self):
        return self._size
