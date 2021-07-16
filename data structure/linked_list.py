"""
    One Way Linked List
"""


class Node:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class LinkedList:
    head = None
    tail = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, value):
        node = Node(value)
        self.count += 1
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def add_to_head(self, value):
        node = Node(value)
        self.count += 1
        if self.head is None:
            self.head = node
        node.next = self.head
        self.head = node

    def remove_at_index(self, target_index):
        if target_index > self.count-1:
            return "index out of range"
        if self.head is None:
            return "Empty!"

        current_node = self.head
        # index = 0
        #
        # while index != target_index:
        #     if index == target_index-1:
        #         to_be_removed = current_node.next
        #         new_next = to_be_removed.next
        #         current_node.next = new_next
        #         index += 1
        #     else:
        #         index += 1
        #         current_node = current_node.next

        for i in range(target_index-1):
            current_node = current_node.next
        current_node.next = current_node.next.next

    def remove_head(self):
        if self.head is None:
            return

        self.count -= 1
        self.head = self.head.next

    def remove_tail(self):
        if self.head is None:
            return

        self.count -= 1
        current_node = self.head
        for i in range(self.count-1):
            current_node = current_node.next
        current_node.next = None

    def add_to_index(self, target_index, value):
        if target_index > self.count-1 or target_index < 0:
            return "index out of range"

        node = Node(value)

        self.count += 1
        current_node = self.head
        for i in range(target_index):
            current_node = current_node.next

        node.next = current_node.next
        current_node.next = node

    def get(self, target_index):
        if target_index > self.count-1:
            return

        current_node = self.head
        for i in range(target_index-1):
            current_node = current_node.next
        return current_node.next.value

    def __str__(self):
        current_node = self.head
        result = []
        while current_node is not None:
            result.append(current_node.value)
            current_node = current_node.next
        return str(result)


li = LinkedList()
li.append(1)
li.append(2)
li.append(3)
li.remove_tail()
print(li.get(1))
