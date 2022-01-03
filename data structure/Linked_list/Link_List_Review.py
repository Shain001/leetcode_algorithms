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

    """
    2021-12-5
    输出链表倒数第k个元素

    注意：
    （1） 对于输入的检查，也即所谓“鲁棒性”。 此题而言即应注意对链表长度是否大于k的检查, 空列表的检查， 输入k= 0 的检查
    （2） 注意对链表中双指针的使用场合和技巧。
    """

    def print_k_(self, k):
        if k == 0:
            return "wrong input"

        if self.head.value is None:
            return "empty list"

        quick_node = self.head
        slow_node = self.head

        count = 0
        while quick_node is not None:
            quick_node = quick_node.next
            if count >= k:
                slow_node = slow_node.next
            count += 1

        if count <= k - 1:
            return "not long enough"

        return quick_node.value

    """
    2012-12-5
    链表反转
    不应使用cur_node is None 为if条件，因为不好记录新的头节点
    """

    def make_list_reverse(self):
        def recursive(pre_node, cur_node):
            if cur_node.next is None:
                cur_node.next = pre_node
                self.head = cur_node
                return

            recursive(cur_node, cur_node.next)
            cur_node.next = pre_node

        if self.head.value is None:
            return "Empty List"

        current_node = self.head
        next_node = current_node.next
        recursive(current_node, next_node)
        current_node.next = None
        return "Reversed"

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

print(li)
li.make_list_reverse()
print(li)

"""
    2021-12-3
    leetcode 2. two sum review
    
    给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

    请你将两个数相加，并以相同形式返回一个表示和的链表。
    
    你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
    
    输入：l1 = [2,4,3], l2 = [5,6,4]
    输出：[7,0,8]
    解释：342 + 465 = 807.
"""


def two_sum(l1, l2):
    """
        2021-12-3
        注意：
        无需迭代
        无需把长度不同的问题写的太复杂。 若两个输入长度不同， 则用0补齐即可

        注意to_return是记录头指针位置的， 而真正的头指针是to_return.next

    :param l1:
    :param l2:
    :return:
    """
    to_return = Node(0)
    cur_node = to_return
    carry = 0
    while l1 is not None or l2 is not None:
        v1 = l1.val if l1 is not None else 0
        v2 = l2.val if l2 is not None else 0
        sum = v1 + v2 + carry

        value = sum % 10
        carry = (sum - value) // 10

        """
        注意此处：第一次进循环时， 即两个输入的第一个节点相加时， 所得的结果存储在 to_return.next 而非to_return本身。
        如果要存到to_return本身的话， 会导致循环结束时产生一个多余节点， e.g. 结果应为7 0 8 但程序会使结果为 7080
        因为如果写成：
            cur_node.value = value
            cur_node.next = Node()
            cur_ = cur.next
        这样在循环结束时， 会不可避免的创建一个多余的next。
        """
        cur_node.next = Node(value)
        cur_node = cur_node.next

        l1 = l1.next if l1 is not None else None

        l2 = l2.next if l2 is not None else None

    if carry != 0:
        cur_node.next = Node(carry)

    return to_return.next


# two_sum测试：
# a = Node(2)
# a.next = Node(4)
# a.next.next = Node(3)
#
# b = Node(5)
# b.next = Node(6)
# b.next.next = Node(4)
#
# head = two_sum(a, b)
#
# while head is not None:
#     print(head.val)
#     head = head.next

def merge_two_ascend_list(head1: Node, head2: Node):
    """
        2021-12-5
        offer 25
    """
    if head1 is None and head2 is None:
        return "invalid head"

    if head1 is None and head2 is not None:
        return head2

    if head2 is None and head1 is not None:
        return head1

    if head1.value > head2.value:
        head = Node(head1.value)
        head1 = head1.next
    else:
        head = Node(head2.value)
        head2 = head2.next

    cur_node = head

    while head1 is not None or head2 is not None:
        value1 = head1.value if head1 is not None else float('-inf')
        value2 = head2.value if head2 is not None else float('-inf')
        if value1 > value2:
            cur_node.next = Node(value1)
            head1 = head1.next
        else:
            cur_node.next = Node(value2)
            head2 = head2.next
        cur_node = cur_node.next

    return head

