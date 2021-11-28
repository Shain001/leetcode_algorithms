"""
链表
2021-11-25
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def append(self, next_node):
        self.next = next_node


class LinkList:
    def __init__(self, head=None):
        self.head = Node(head)
        self.size = 0 if head is None else 1

    def add(self, node_value):
        node = Node(node_value)
        self.size += 1

        if self.head.value is None:
            self.head = node
            return

        tail = self.get_tail()
        tail.next = node
        return

    def get_tail(self) -> Node:
        node = self.head

        while node.next is not None:
            node = node.next
        return node


    def reverse_print_recursion(self):
        def recursion(node: Node):
            if node.next is None:
                print(node.value)
                return

            recursion(node.next)
            print(node.value)

        head_node = self.head
        recursion(head_node)

    def reverse_print_non_recursion(self):
        if self.head.value is None:
            print("Empty Link List")
        stack = []
        node = self.head
        while node.next is not None:
            stack.append(node.value)
            node = node.next
        stack.append(node.value)
        while len(stack) > 0:
            print(stack.pop(-1))

    def __str__(self):
        to_return = []
        node = self.head
        while node.next is not None:
            to_return.append(node.value)
            node = node.next

        # !!! dont forget this, without this you will lose one value
        to_return.append(node.value)
        return str(to_return)


li = LinkList()
for i in range(1, 5):
    li.add(i)

li.reverse_print_recursion()
