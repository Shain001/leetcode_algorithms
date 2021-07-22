"""
    using Linked List to implement Stack
"""
from Linked_list import *


class Stack:
    def __init__(self):
        self.head = Node()
        self.count = 0

    def check_empty(self):
        return self.count == 0

    def push(self, value):
        if self.check_empty():
            self.head.next = Node(value)
            self.count += 1
        else:
            temp = self.head.next
            self.head.next = Node(value)
            self.head.next.next = temp
            self.count += 1

    def pop(self):
        if self.check_empty():
            return "empty"
        node = self.head.next
        self.head.next = node.next
        self.count -= 1
        return node.value


# stack = Stack()
# for i in range(5):
#     print(i)
#     stack.push(i)
#
#
# for i in range(5):
#     print(stack.pop())