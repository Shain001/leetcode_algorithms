class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0

    def get_tail(self):
        node = self.head
        while node.next is not None:
            node = node.next
        return node

    def append(self, value):
        if self.size == 0:
            self.head.next = Node(value)
            self.size += 1
        else:
            self.get_tail().next = Node(value)
            self.size += 1

    def append_node(self, node):
        if self.size == 0:
            self.head.next = node
            self.size += 1
        else:
            self.get_tail().next = node
            self.size += 1

    def __str__(self):
        values = []
        if self.size == 0:
            return "empty"
        node = self.head.next
        while node.next is not None:
            values.append(node.value)
            node = node.next
        values.append(node.value)
        return str(values)
