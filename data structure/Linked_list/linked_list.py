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

    def reverse(self, curr):
        """
            In one word, when you do the recursive method:
            1. Identify the function of this method and 'identify the return value' --> 反转每个node, 返回一个node
            2. Identify the basic return condition --> 找到最后一个node
            3. Then the function part(pre = .. pre.next = ..) 会被倒序执行，即从最后一个node开始执行
            4. Therefore, we just need to identify what is the process that each node (or from higher level, each elements)
               should be implemented
            5. Also one thing is important is to identify the first returned element
            此问题中：
            目的为反转列表， 最先返回的是倒数第一个node，且每个node的执行操作都一致：
            即将后一个node 的next设为前一个node，即程序中的当前node， 然后将程序中的当前node的next指针清0
        """
        if curr.next is None:
            # 更新头指针，使其指向新的头节点
            self.head.next = curr
            return curr
        # 程序会卡在这里，反复调用自己，直到找到最后一个node
        # 找到之后，pre会从最后一个node开始，依次变成前一个node,而不是再此调用自己，这就是为什么curr.next为null了
        # 但是不会再此执行if
        next_node_in_unreversed = self.reverse(curr.next)
        next_node_in_unreversed.next = curr
        curr.next = None

        return curr


li = LinkedList()
li.append(5)
li.append(4)
li.append(3)
li.append(2)
li.append(1)
li.reverse(li.head.next)
print(li)

