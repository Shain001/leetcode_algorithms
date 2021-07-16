"""
    Two Way Linked List
"""


class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class TwoWayLink:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_to_head(self, value):
        node = Node(value)
        if self.check_empty():
            self.head = node
            self.size += 1
            self.tail = node
            return
        self.size += 1
        node.next = self.head
        self.head.prev = node
        self.head = node

    def add_to_tail(self, value):

        node = Node(value)
        if self.check_empty():
            self.head = node
            self.size += 1
            return

        self.size += 1
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def insert(self, value, target_index):
        self.size += 1
        node = Node(value)
        current_node = self.head
        for _ in range(target_index-1):
            current_node = current_node.next
        next_node = current_node.next
        current_node.next = node
        node.prev = current_node
        node.next = next_node
        next_node.prev = node

    def remove(self, index):
        if index > self.size-1:
            return
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        next_node = current_node.next
        prev_node = current_node.prev
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def remove_head(self):
        if self.check_empty():
            return

        self.size -= 1
        self.head = self.head.next
        self.head.prev = None

    def remove_tail(self):
        if self.check_empty():
            return
        self.size -= 1
        prev = self.tail.prev
        self.tail = prev
        self.tail.next = None

    def get(self, index):
        if self.check_empty() or index > self.size-1:
            return

        current = self.head
        for _ in range(index-1):
            current = current.next
        return current.value

    def search(self, value):
        if self.check_empty():
            return

        cur = self.head
        for i in range(self.size):
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def check_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def __str__(self):
        current_node = self.head
        result = []
        while current_node is not None:
            result.append(current_node.value)
            current_node = current_node.next
        return str(result)


li = TwoWayLink()
li.add_to_head(1)
li.add_to_tail(2)
li.insert(3,1)

print(li.search(2))